from django.shortcuts import render,redirect
from . forms import tr_form
from . models import traveller_det
def home(request):
    fm = ''
    if request.method == 'POST' or None:
        fm = tr_form(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = traveller_det()
        data = traveller_det.objects.all()
    return render(request,'home.html',{'fm':fm,'data':data})
