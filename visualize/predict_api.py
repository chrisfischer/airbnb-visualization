import numpy as np
from .models import Listing

# handles the differnt options of this api
def predict_handler(o):
    if 'price' in o:
        return get_best_price(o)
    elif 'income' in o:
        return get_income(o)

# gets the optimal price for max revenue at a location and returns that price
def get_best_price(o):

    # find properties nearby
    # find ones with lowest availability and highest value
    # return averaged price

    coords = o['price'][0].split(' ')
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
    price = round(np.mean([d['price'] for d in results[:20]]), 2)
    
    return price

# helper for get_best_price
def calculate_weighted_sum(d):
    availability_weight = (1/60) * 0.5
    review_scores_weight = (1/10) * 0.7

    aval = (60 - d['availability_60']) * availability_weight
    revs = d['review_scores_value'] * review_scores_weight

    return aval + revs

# returns the estimated weekly income
def get_income(o):

    # find best price following above procedure
    # multiply that by 7
    # multiply that by the average occupancy rate
    # subtract average weekly morgage cost

    coords = o['income'][0].split(' ')
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
    weighted = [{ 'price': d['price'], 'weight': calculate_weighted_sum(d)} for d in results]

    # sort by highest weighted sum and price
    weighted = sorted(weighted, key=lambda d: (d['weight'],d['price']), reverse=True)

    # average price of top 20
    price = np.mean([d['price'] for d in weighted[:20]])
    occupancy = np.mean([1-d['availability_60']/60.0 for d in results[:20]])
    
    revenue = round(float(price) * 7.0 * occupancy, 2)

    return revenue

    