# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connections
from django.db.models import Count
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import os

from .models import Listing

# Create your views here.

def graph(request):
    return render(request, 'graph.html')

def heat_map(request):
    return render(request, 'map.html')

def predict(request):
    return render(request, 'predict.html')

def api(request):
    url = request.META['PATH_INFO']
    o = dict(request.GET)
    options = {}
    options['fields'] = o['fields'][0].split(' ')
   
    if 'plot' in o:
        options['plot'] = {}
        if o['plot'][0] == 'xy':
            options['plot']['x'] = F(options['fields'][0])
            options['plot']['y'] = F(options['fields'][1])
        elif o['plot'][0] == 'yx':
            options['plot']['x'] = F(options['fields'][1])
            options['plot']['y'] = F(options['fields'][0])
        else:
            return None
        options['null'] = {}
        options['null']['x__isnull'] = True 
        options['null']['y__isnull'] = True
        results = list(Listing.objects.annotate(**options['plot']).exclude(**options['null']).values('x', 'y'))
        results = [r for r in results if not r['x'] is None and not r['y'] is None]
        return JsonResponse(results, safe=False)

    else:
        results = list(Listing.objects.values(*options['fields']))
        return JsonResponse(results, safe=False)