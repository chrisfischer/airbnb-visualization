import numpy as np
import re

from collections import defaultdict
from django.db.models import F
from django.db.models.functions import Length
from .models import Listing

'''
API - offers a way to pull data from the database:
    fields: fields from models.Listing to be queried

    plot: Lets you create aliases for variables. Need the same number of aliases as fields. Also filters null values.

    groupBy: currently only groups by location, will average the given field(s) by a 0.001 square degree regions and return either: (1) a tuple of the average value and coordinates if only one field was passed in, or (2) a tuple of coordinates and a dictionary of field name -> average value. Also filters null values.

    Other options:
        length(field): will create an alias length_field with the length of that character field

'''

def parse_get(o):
    options = {}
    options['annotate'] = {}
    options['null'] = {}
    options['fields'] = o['fields'][0].split(' ')

    # return list of numerical fields
    if (options['fields'][0] == 'numericalFields'):
        return Listing.get_numerical_fields()

    for i, f in enumerate(options['fields']):
        parts = re.split(r'\(|\)', f)
        if len(parts) > 1:
            del options['fields'][i]
            func = parts[0]
            var = parts[1]
            if func == 'length':
                options['annotate']['length_' + var] = Length(var)
                options['fields'].append('length_' + var)

    # check if plot fields were given
    if 'plot' in o:
        # get the given alias names
        variables = o['plot'][0].split(' ')
        for i, v in enumerate(variables):
            # creates the aliases
            options['annotate'][v] = F(options['fields'][i])
            # filter null values
            options['null'][v + '__isnull'] = False

        print (options)
        # retrieve results
        results = list(Listing.objects.annotate(**options['annotate']).filter(**options['null']).values(*variables))
       
        return results

    # check if group by fields were given
    if 'groupBy' in o:
        # currently only supports location grouping

        oldFields = options['fields']
        if o['groupBy'][0] == 'location':
            if len(options['fields']) == 1:
                # only one field, change alias to 'weight'
                options['annotate']['weight'] = F(options['fields'][0])
                options['fields'] = ['weight']
            
            # add lat and log to coorinates to be queried
            options['fields'].append('latitude')
            options['fields'].append('longitude')

            # filter null values
            for i, v in enumerate(options['fields']):
                options['null'][v + '__isnull'] = False
            
            print (options)
            # retrieve results
            results = list(Listing.objects.annotate(**options['annotate']).filter(**options['null']).values(*options['fields']))

            return average_results_by_location(results, oldFields)

    # standard data return
    else:
        # retrieve results
        print (options)
        results = list(Listing.objects.annotate(**options['annotate']).values(*options['fields']))
        return results

# helper function for grouping by location
def average_results_by_location(results, fields):
    # values maps coords -> (field -> list of values)
    values = defaultdict(lambda: defaultdict(list))
    print(fields)
    if (len(fields) == 1 and 'length_house_rules' == fields[0]):
        print('_____________________reached')
        precision = 400
    else:
        precision = 1000

    for r in results:

        coords = str(round_nearest(r['latitude'], precision)) + ' ' + str(round_nearest(r['longitude'], precision))
        for k, v in r.items():
            if k == 'latitude' or k == 'longitude':
                continue
            values[coords][k].append(v)

    # to_return is a list of (coords, value) or (coords, dict of fields -> value)
    to_return = []
    for k1, v1 in values.items():
        d = {}
        for k2, v2 in v1.items():
            d[k2] = np.mean(v2)
        if len(d) == 1:
            to_return.append((k1, list(d.values())[0]))
        else:
            to_return.append((k1, d))
        
    return to_return

# default rounds to the nearest 1/1000
def round_nearest(x,num=1000):
    return round(x * num) / num
