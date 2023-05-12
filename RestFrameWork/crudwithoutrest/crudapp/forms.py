from django import forms
from . models import Employee
from django.forms import ValidationError


class EmployeeForm(forms.ModelForm):
    def clean_sal(self): #Field validation
        inputsal = self.cleaned_data['esal']
        if inputsal<=5000:
            raise forms.ValidationError('the min sal should be 5000')
        return inputsal
    class Meta:
        model = Employee
        fields = '__all__'
