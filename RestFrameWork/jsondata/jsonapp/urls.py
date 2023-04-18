from django.urls import path
from .import views

urlpatterns = [
    path('home',views.home),
    path('apijsonCBV',views.jsonCBV.as_view())
]
