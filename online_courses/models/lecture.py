from django.db import models
from online_courses.models.course import Course


class Lecture(models.Model):
    theme = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='lectures/', null=True)