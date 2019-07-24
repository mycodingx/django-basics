from django.shortcuts import render
from . import forms


# Create your views here.

def index(request):
    form = forms.Student()

    if request.method == 'POST':
        form = forms.Student(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("ADDRESS: " + form.cleaned_data['address'])
    return render(request, 'student/index.html', {'form': form})
