# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from .models import Girls,Areas
# Create your views here.

from django.http import HttpResponse


def index(request):
        return render(request, 'banks/index.html')

def query(request):
    if request.GET.get('area', ''):
        area = request.GET.get('area', '')
        girls = Girls.objects.filter(area__contains=area)
        area = Areas.objects.filter(area__contains=area)[0]
        s = '{"area":["lat":"'+area.lat+'","lon":"'+area.lon+'"],"girls":[';
        for girl in girls:
            s+='{ "name" : "'+girl.name+'",'
            s+='"age" : "'+girl.age+'",'
            s+='"area" : "'+girl.area+'",'
            s+='"lat" : "'+girl.lat+'",'
            s+='"lon" : "'+girl.lon+'" },'
        s = s[:-1]
        s+=']}'


    return HttpResponse(json.dumps(s), content_type='application/json')
