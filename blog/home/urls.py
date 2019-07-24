from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog', views.blog, name="blog"),
    path('register', views.register, name="blog"),
]
