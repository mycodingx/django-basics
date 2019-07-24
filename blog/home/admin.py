from django.contrib import admin
from home.models import AccessRecord, Topic, Webpage, PostCategory, Post, Student

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(PostCategory)
admin.site.register(Post)
admin.site.register(Student)
