

from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def student1(request):
    return HttpResponse("Student name")
def greet(request,name):
    return HttpResponse(f"Hello,{name}")