from django import forms
from home.models import Student


class NewStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
