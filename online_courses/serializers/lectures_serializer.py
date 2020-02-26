from rest_framework import serializers
from online_courses.models.lecture import Lecture


class Lecture_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = ('theme', 'course', 'file')