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

### Create FIrst Django Plugable App

Create your first plugable app uisng 
```
python manage.py startapp home
```