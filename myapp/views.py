from django.shortcuts import render
from django.http import HttpResponse

def firstView(request):
    details = {"name":'priya' , "Age":10}
    return render(request,'login.html',details)

def secondView(request):
    return render(request,'signup.html')

