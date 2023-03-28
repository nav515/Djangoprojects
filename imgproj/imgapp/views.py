from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import UploadImage

# Create your views here.\
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance
            return render(request, 'img_form.html', {'form': form, 'img_obj': img_object})
    else:
        form = ImageForm()
    return render(request,'img_form.html',{'form': form})
