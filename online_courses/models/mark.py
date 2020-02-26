from django.db import models
from django.core.validators import MaxValueValidator


class Mark(models.Model):
    digit = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
