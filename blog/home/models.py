from django.db import models


# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, )
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey('Webpage', on_delete=models.CASCADE, )
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class PostCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to='images/');
    category = models.ForeignKey('PostCategory', on_delete=models.CASCADE, )
    date = models.DateField()

    def __str__(self):
        return str(self.title)


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return str(self.name)
