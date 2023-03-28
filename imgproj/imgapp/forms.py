from django.forms import ModelForm
from .models import UploadImage

class ImageForm(ModelForm):
    class Meta:
        model = UploadImage
        fields = '__all__'