from django.urls import path
from . views import home,read,edit,delete

urlpatterns = [
    path('',home,name='home'),
    path('read',read,name='read'),
    path('update/<int:id>/',edit,name='edit'),
    path('delete/<int:id>/',delete,name='delete')
]
