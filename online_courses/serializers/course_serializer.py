from rest_framework import serializers
from online_courses.models.course import Course
from online_courses.serializers.user_serializer import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
    teachers = UserSerializer.UserSerializer(read_only=True, many=True)
    students = UserSerializer.UserSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'teachers', 'students')
        read_only_fields = ('id',)