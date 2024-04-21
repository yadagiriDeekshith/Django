from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def addition(request):
    if request.method == 'POST':
        num1=int(request.POST['t1'])
        num2=int(request.POST['t2'])
        res=num1+num2
        return render(request,'result.html',{'result':res})
    
    return render(request,'addition.html')