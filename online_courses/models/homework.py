from django.db import models
from django.contrib.auth.models import User
from online_courses.models.lecture import Lecture


class Homework(models.model):
    task = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')