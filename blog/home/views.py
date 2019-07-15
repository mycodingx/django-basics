from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
"""
def index(request):
    return HttpResponse("Hello World!")
"""

def index(request):
    data_dict = {'insert_data':"Hello from Django template tag"}
    return render(request,'home/index.html',context=data_dict)

