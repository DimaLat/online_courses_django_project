from rest_framework import serializers
from online_courses.models.mark import Mark


class Mark_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = ('digit',)