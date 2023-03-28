from django.urls import path
from .views import datashow

urlpatterns = [
    path('',datashow,name='form'),
]
