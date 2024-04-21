from django.shortcuts import render
from django.http import HttpResponse
def display(request):
    obj=render(request,'hello.html',{'inst_name':'VCube'})
    return obj

# Create your views here.
