import datetime
from time import strftime

from django.shortcuts import render

# Create your views here.

def hellohtml(request):
    name = 'Hello Naveen Gopagani '
    firstname = 'Naveen'
    lastname = 'Kumar'
    mobile_number = 9010579202
    date = datetime.datetime.now()
    datetm = strftime("%H")
    if int(datetm) < 12:
        name = name + ' Good Mrng'
    if int(datetm) >12 and int(datetm) <=16 :
        name = name + ' Good afterNoon'
    else:
        name = name + ' Good Night'
    data = {'name':name,'firstname':firstname,'lastname':lastname,'mobile_number':mobile_number,'date':date}
    return render(request, "home.html",data)
