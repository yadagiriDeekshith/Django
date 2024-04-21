from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def getApi(request):
    d={
        'name':'Deekshith',
        'age':23,
        'gender':None

    }
    data = json.dumps(d)
    return JsonResponse(data,safe=False)