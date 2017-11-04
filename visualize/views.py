# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connections
from django.shortcuts import render
from django.db.models import Count
from django.db.models import F
from django.http import JsonResponse, HttpResponse
from django.template.response import TemplateResponse


from .models import Listing

from .api import parse_get
from .predict_api import predict_handler

# Create your views here.

def index(request):
    return render(request, 'index.html')

def scatter(request):
    exclude = []
    kv = [(k,v) for k,v in Listing.get_numerical_fields().items() if not k in exclude]
    kv = dict(kv)
    return TemplateResponse(request, 'scatter.html', {'data': {'keys': kv.keys(), 'values':kv.values()}})

def heat_map(request):
    exclude = ['Price', 'Bedrooms', 'Bathrooms', 'Square Feet', 'Num. Reviews', 'Len. House Rules']
    kv = [(k,v) for k,v in Listing.get_numerical_fields().items() if not k in exclude]
    kv = dict(kv)
    return TemplateResponse(request, 'map.html', {'data': {'keys': kv.keys(), 'values':kv.values()}})

def optimize(request):
    return render(request, 'optimize.html')

def estimate(request):
    return render(request, 'estimate.html')

def api(request):
    url = request.META['PATH_INFO']
    o = dict(request.GET)
    results = parse_get(o)
    return JsonResponse(results, safe=False)

def predict_api(request):
    url = request.META['PATH_INFO']
    o = dict(request.GET)
    results = predict_handler(o)
    return JsonResponse(results, safe=False)

