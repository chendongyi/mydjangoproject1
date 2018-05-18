# coding:utf-8
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def extends1(request):
    return render(request,'extends1.html')