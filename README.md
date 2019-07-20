# Django Basics

Get up and running with Django

## Level One

How to install and setup your first Django project

### Prerequisites

Install [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=windows) and [Anaconda(optional)](https://www.anaconda.com/distribution/) before you follow the below given steps.

### Setup and Run First Project

Once you have downloaded and installed all the required tools follow the below given steps:

* Craete a new project using Pycharm and setup your virtual environment using additional options.

* Then install the Django package using the command 

If you are using conda 
```
conda install django  
```

If you are using pip 
```
pip install django
```

* Now create a Django project using django-admin
```
django-admin startproject blog
```

* Now go into your directory which contains "manage.py" file and start your server 
```
python manage.py runserver
```

### Create First Django Plugable App

* Create your first plugable app uisng 
```
python manage.py startapp home
```

* Now add your first app to INSTALLED_APPS in settings.py file
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home'
]
```

* Now create a view for our first app in views.py file
```
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")
```

* Now add view url to url.py file
```
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name="index"),
    path('admin/', admin.site.urls),
]
```

##Level Two

Creating Model and getting data from database

### Adding Models

* First Create model class in the model.py class of your app folder and then run the "migrate" command
```buildoutcfg
python manage.py migrate
```
* Then run the "makemigrations" command for your python app
```buildoutcfg
python manage.py makemigrations home
```
* Now you have to create a superuser who can access the database using python admin panel
```buildoutcfg
python manage.py createsuperuser
```

### Using python faker library
Fake library is used to populate your database with some dummy data automatically. If you are following this series then you can find "populate_home_app.py" file in the project base directory you can use that file to populate your database with dummy data.

* Install Faker
```buildoutcfg
pip install faker
```

* Populate database with fake data
```buildoutcfg
python populate_home_app.py
``` 

### Step to fetch and display data in your HTML templates
* **First**: In the views.py file we import any models that we will need to use.
* **Second**: Use the view to query the model for data that we will need.
* **Third**: Pass results from the model to the template.
* **Fourth**: Edit the template so that it is ready to accept and display the data from the model.
* **Fifth**: Map a URL to the view.



