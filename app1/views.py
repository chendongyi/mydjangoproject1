# coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
def index(request):
    #return HttpResponse(u"Welcome to Chen Dongyi's HomePage")
    return render(request,'app1_home.html')
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def old_index_redeirect(request):
    return HttpResponseRedirect(reverse('app1_index'))