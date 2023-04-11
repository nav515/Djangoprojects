from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import datetime
from time import strftime
from django.contrib import messages


def home(request):
    name = 'New User'
    date = datetime.datetime.now()
    datetm = strftime("%H")
    if int(datetm) < 12:
        name = ' Good Morning'
    if int(datetm) >12 and int(datetm) <=16 :
        name = ' Good afterNoon'
    if int(datetm) >16 and int(datetm) <=18 :
        name = ' Good Evening'
    if int(datetm)>18  and int(datetm) <=24 :
        name = ' Good night'
    data = {'name':name,'date':date}
    return render(request,'home.html',data)


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        email_list = list(User.objects.values_list("email", flat=True))

        if user is not None:
            print('hello naveen')
            print('pPPPPPPPPPPPPPPPPPP',email_list)
            print('UUUUUUUUUUUUUUU',user.username)
            print('EEEEEEEEEEEEEEEEEEEE',user.password)
            auth.login(request,user)
            messages.success(request, 'login successfully.')
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                print('username already taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                print('Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,email=email, password=password1)
                user.save()
                messages.info(request, 'user created pls lagin')
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'password not matched')
            print('password not matched')
            return redirect('register')
    return render(request,'register.html')
