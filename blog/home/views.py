from django.shortcuts import render
from home.models import Topic, Webpage, AccessRecord, PostCategory, Post
from home.forms import NewStudent

# Create your views here.
"""
def index(request):
    return HttpResponse("Hello World!")
"""


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    data_dict = {'access_records': webpages_list}
    return render(request, 'home/index.html', context=data_dict)


def blog(request):
    blog_list = Post.objects.order_by('date')
    data_dict = {'posts': blog_list}
    return render(request, 'home/blog.html', context=data_dict)


def register(request):
    form = NewStudent()

    if request.method == 'POST':
        form = NewStudent(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error!!')

    return render(request, 'home/register.html', {'form': form})
