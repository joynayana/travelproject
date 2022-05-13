from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from vlogapp.views import current

# Create your views here.
def fun(request):
    obj=place.objects.all()
    data=current.objects.all()
    return render(request,"index.html",{'results':obj,'out':data})

def addition(request):
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    sum=val1+val2
    return render(request,'result.html',{'result':sum})