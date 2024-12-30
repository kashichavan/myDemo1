from django import forms
from .models import Student,Car

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields='__all__'
