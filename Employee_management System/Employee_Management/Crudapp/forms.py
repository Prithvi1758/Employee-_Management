from django.forms import ModelForm
from .models import Student

class Student_from(ModelForm):
    class Meta:
        model=Student
        fields="__all__"