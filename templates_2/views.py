# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    string = u"我在自强学堂学习django，用它来建网站"
    return render(request, 'tempates_2/home.html',{'string':string})

def tutorlist(request):
    TurtorialList = ["HTML","CSS","jQuery","Python","Django",]
    return render(request, 'tempates_2/list.html',{'TurtorialList':TurtorialList})

def dict(request):
    info_dict = {'site':u'自强学堂','content':u'各种IT技术教程',}
    return render(request,'tempates_2/dict.html',{'info_dict':info_dict})

def listfor(request):
    List = map(str, range(100))
    return render(request,'tempates_2/listfor.html',{'List':List})

def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))