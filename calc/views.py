from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("hello world")
    return render(request,"home.html",{'name':"amitoj"})

def add(request):
    v1=request.POST["first"]
    v2=request.POST["second"]
    res=int(v1)+int(v2)

    return render(request,'result.html',{'result':res})