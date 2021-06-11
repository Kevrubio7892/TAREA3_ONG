from django.contrib import admin
from django.urls import path, include
from .views import index,gatos,perros,coraje,doraemon,garfield,patan,scooby,tom

urlpatterns = [
    path('',index,name='IND'),
    path('gatos/',gatos,name='GAT'),
    path('perros/',perros,name='PERR'),
    path('coraje/',coraje,name='COR'),
    path('doraemon/',doraemon,name='DOR'),
    path('garfield/',garfield,name='GAR'),
    path('patan/',patan,name='PAT'),
    path('scooby/',scooby,name='SCO'),
    path('tom/',tom,name='TOM'),

]