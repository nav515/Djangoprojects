from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('api/<int:id>/',views.EmpjsonCBV.as_view()),
    path('api/',views.EmpListCBV.as_view())
]
