from django.shortcuts import render,redirect
from . models import Registration
from . forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def Registrationview(request):
    form = RegistrationForm()
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        user = Registration(uname=uname, email=email)

        domain_name = get_current_site(request).domain
        print('**********************',domain_name)
        token = str(random.random()).split('.')[1]
        print("********************",token)
        user.token = token
        link = f'http://{domain_name}/verify/{token}'
        htmlTrippleQuoted = f"""
        <html>
        <head>
        </head>
        <body>
        <div id='title'>
        <h1>Hai Naveen </h1>
        <a href='{link}'>click-chey ra {link}</a>
        </div>
        </body>
        </html>"""

        send_mail(
                  'Email Verification',
                  'Hi',
                  settings.EMAIL_HOST_USER,
                  ['naveengopagani835@gmail.com'],
                  fail_silently=False,
                  html_message=htmlTrippleQuoted

                  )

        #http://my-domain.com/verify/<token>
        return HttpResponse('this email has been sent')
    return render(request, 'register.html', {'form': form})

def verify(request,token):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@ Run raja1111")
    try:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@ Run raja2222")
        user = Registration.objects.filter(token=token)
        print('qwertgggggggggggg',user)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@ Run ")
        if True:
            user.is_verified =True
            msg ='your email has been verified'
            return render(request,'home.html',{'msg':msg})
    except Exception as e:
        msg = e
        return render(request,'info.html',{'msg':msg})
    return(request,'home.html')