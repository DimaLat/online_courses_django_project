from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=30)
    students = models.ManyToManyField(User, related_name='students', blank=True)
    teachers = models.ManyToManyField(User, related_name='teachers')