from django.shortcuts import render
from home.models import Topic,Webpage,AccessRecord
# Create your views here.
"""
def index(request):
    return HttpResponse("Hello World!")
"""

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    data_dict = {'access_records':webpages_list}
    return render(request,'home/index.html',context=data_dict)

