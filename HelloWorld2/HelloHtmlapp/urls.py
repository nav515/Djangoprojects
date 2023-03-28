from django.urls import path,include
from .views import hellohtml

urlpatterns = [
    path('',hellohtml,name='hello')
]
