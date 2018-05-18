"""mydjango1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1 import views as app1_views #new
from templates_app import views as templates_views
from templates_2 import views as tmp_2
from formexample import views as formexample
urlpatterns = [
    #url(r'^tempates_2/home/$',tmp_2.home,name='home'),
    #url(r'^tempates_2/list/$',tmp_2.tutorlist,name='list'),
    #url(r'^tempates_2/dict/$',tmp_2.dict,name='dict'),
    #url(r'^tempates_2/listfor/$', tmp_2.listfor, name='listfor'),
    #url(r'^tempates_2/add/(\d+)/(\d+)$',tmp_2.add,name='add'),
    #url(r'^add/$',app1_views.add, name='add'), #new
    #url(r'^new/$',app1_views.index,name='app1_index'),
    #url(r'^$',templates_views.home, name='home'),
    #url(r'^new_index/$',app1_views.old_index_redeirect),
    #url(r'^extends1/$',templates_views.extends1),
    url(r'^$',formexample.index, name='home'),
    url(r'^admin/', admin.site.urls),
]
