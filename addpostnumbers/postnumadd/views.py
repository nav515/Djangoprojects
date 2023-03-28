from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'index.html')
def add(request):
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        res = num1+num2
    return render(request,'index.html',{'res':res})
