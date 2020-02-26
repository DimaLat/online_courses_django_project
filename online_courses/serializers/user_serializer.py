from django.contrib.auth.models import User
from rest_framework import serializers


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'firstname', 'lastname', 'password', 'role')