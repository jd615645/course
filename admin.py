from django.contrib import admin
from apps.course.models import Course_of_user, Course
# Register your models here.
admin.site.register(Course_of_user)
admin.site.register(Course)
