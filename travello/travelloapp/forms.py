from django.forms import ModelForm
from .models import traveller_det

class tr_form(ModelForm):
    # specify the name of model to use
    class Meta:
        model = traveller_det
        fields = "__all__"