from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . forms import EmployeeForm
from . models import Employee
from django.contrib import messages
# Create your views here.
def datashow(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form = EmployeeForm()
            messages.success(request, ' Form submitted successfully.')
            data = Employee.objects.all().order_by('EmpNum')
            return render(request,'home.html',{'form': EmployeeForm(request.GET),'data':data})
    # if a GET (or any other method) we'll create a blank form
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = EmployeeForm()
        data = Employee.objects.all().order_by('EmpNum')
    return render(request,'home.html',{'form': form,'data':data})
