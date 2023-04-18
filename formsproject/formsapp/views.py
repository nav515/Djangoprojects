from django.shortcuts import render,redirect
from . forms import StudentForm
from . models import Student
# Create your views here.
def home(request):
    fm=''
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = StudentForm()
        data = Student.objects.all().order_by('-id')
    return render(request,'home.html',{'fm':fm,'data':data})

def read(request):
    data = Student.objects.all()
    return render(request,'read.html',{'data':data})

def edit(request,id):

    dataget = Student.objects.get(id=id)
    print('dataget:---------------',dataget)
    data = Student.objects.all()
    fm = StudentForm(instance = dataget)
    print('fm data----------------',fm)
    if request.method == 'POST':
        fm = StudentForm(request.POST,instance = dataget)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    return render(request,'home.html',{'fm':fm,'data':data})
def delete(request,id):
    dataget = Student.objects.get(id=id)
    dataget.delete()
    return redirect('home')