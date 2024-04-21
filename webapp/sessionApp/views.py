from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sessionExample(request):
    if 'cnt' in request.session:
        request.session['cnt']+=1
    else:
        request.session['cnt']=1

    return HttpResponse('Request count' +str(request.session['cnt']))

def storeData(request):
    return render(request,'sessionApp/firse.html')