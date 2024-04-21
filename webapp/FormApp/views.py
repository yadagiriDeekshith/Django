from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def FirstForm(request):
    emptyForm = FirstForm()
    if request.method == 'POST':
        dataForm=FirstForm(request.POST)
        if dataForm.is_valid()==True:
            n1=dataForm.cleaned_data['value1']
            n2=dataForm.cleaned_data['value2']
            msg='values recived are ['+n1+','+n2+']'
            return render(request,'FormApp/first.html',{'form':emptyForm,'message':msg})
    return render(request,'FormApp/first.html',{'form':emptyForm})


def insertModelForm(request):
    return render(request,'FormApp/insertModel.html')