import numpy as np

from collections import defaultdict
from django.db.models import F
from .models import Listing

def parse_get(o):
    options = {}
    options['fields'] = o['fields'][0].split(' ')

    if 'plot' in o:
        options['plot'] = {}
        options['null'] = {}
        variables = o['plot'][0].split(' ')
        for i, v in enumerate(variables):
            options['plot'][v] = F(options['fields'][i])
            options['null'][v + '__isnull'] = False

        print (options)
        results = list(Listing.objects.annotate(**options['plot']).filter(**options['null']).values(*variables))
       
        return results

    if 'groupBy' in o:
        if o['groupBy'][0] == 'location':
            options['plot'] = {}
            if len(options['fields']) == 1:
                # only one field, change alias to 'weight'
                options['plot']['weight'] = F(options['fields'][0])
                options['fields'] = ['weight']
            
            options['fields'].append('latitude')
            options['fields'].append('longitude')

            options['null'] = {}
            for i, v in enumerate(options['fields']):
                options['null'][v + '__isnull'] = False
            
            print (options)
            results = list(Listing.objects.annotate(**options['plot']).filter(**options['null']).values(*options['fields']))

            return average_results_by_location(results)

            return results

    else:
        results = list(Listing.objects.values(*options['fields']))
        return results

def average_results_by_location(results):

    values = defaultdict(lambda: defaultdict(list))

    for r in results:
        coords = str(round(r['latitude'], 3)) + ' ' + str(round(r['longitude'], 3))
        for k, v in r.items():
            if k == 'latitude' or k == 'longitude':
                continue

            values[coords][k].append(v)

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




