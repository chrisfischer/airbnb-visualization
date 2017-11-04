import numpy as np
from .models import Listing

def get_best_price(o):
    # find properties nearby
    # find ones with lowest availability and highest value
    # return averaged price

    coords = o['coords'][0].split(' ')
    lat = float(coords[0])
    lng = float(coords[1])

    fields = ['availability_60', 'review_scores_value', 'price']

    filters = {
        'latitude__gte': lat-0.005,
        'latitude__lte': lat+0.005,
        'longitude__gte': lng-0.005,
        'longitude__lte': lng+0.005,
        'availability_60__isnull': False,
        'review_scores_value__isnull': False,
        'price__isnull': False,
    }

    # query database
    results = list(Listing.objects.filter(**filters).values(*fields))

    # calculate weighted sum
    results = [{ 'price': d['price'], 'weight': calculate_weighted_sum(d)} for d in results]

    # sort by highest weighted sum and price
    results = sorted(results, key=lambda d: (d['weight'],d['price']), reverse=True)

    # average price of top 20
    price = np.mean([d['price'] for d in results[:20]])
    
    return price


def calculate_weighted_sum(d):
    availability_weight = (1/60) * 0.5
    review_scores_weight = (1/10) * 0.7

    aval = (60 - d['availability_60']) * availability_weight
    revs = d['review_scores_value'] * review_scores_weight

    return aval + revs