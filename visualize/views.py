# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connections
from django.shortcuts import render
from django.db.models import Count
from django.db.models import F
from django.http import JsonResponse
from django.http import HttpResponse

from .models import Listing

from .api import parse_get

# Create your views here.

def test(request):
    return render(request, 'tables.html')

def graph(request):
    return render(request, 'graph.html')

def heat_map(request):
    return render(request, 'map.html')

def predict(request):
    return render(request, 'predict.html')

def api(request):
    url = request.META['PATH_INFO']
    o = dict(request.GET)
    results = parse_get(o)
    return JsonResponse(results, safe=False)

