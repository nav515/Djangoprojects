from django.urls import path
from .views import home,Registrationview,verify

urlpatterns = [
    path('',home,name='home'),
    path('register',Registrationview,name='register'),
    path('verify/<str:token>',verify),
]
