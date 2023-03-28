from django.shortcuts import render
from . forms import EmployeeForm
from . models import Employee
# Create your views here.
def datashow(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmployeeForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            data = Employee.objects.all()
            return render(request, 'home.html', {'form': form, 'data':data})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmployeeForm()
    return render(request,'home.html',{'form': form})