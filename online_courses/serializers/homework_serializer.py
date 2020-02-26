from rest_framework import serializers
from online_courses.models.homework import Homework


class Homework_serializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('task', 'lecture', 'teacher')