from django.shortcuts import render
from django.http import HttpResponse

def firstView(request):
    data ={'name':'Riyaz','age':23}
    return render(request,'login.html',data)

def secondView(request):
    return render(request,'signup.html')

