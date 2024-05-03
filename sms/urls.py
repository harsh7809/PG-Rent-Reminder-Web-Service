from django.contrib import admin
from django.urls import path 
from sms import views


urlpatterns = [ 
     path('', views.index, name='home'),  
     path('ser', views.service, name='service'),
     path('sms', views.sms, name='sms'),
     path('all', views.all_alert, name='all')


]