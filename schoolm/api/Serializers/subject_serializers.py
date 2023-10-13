from rest_framework import serializers
from ..models import *
from .user_serializer import UserSerializer

class SubjectSerializer(serializers.ModelSerializer):


    teacher = UserSerializer()

    class Meta:
        model = Subject
        fields = "__all__"

    def create(self, validated_data):
        teacher_data = validated_data.pop('teacher')
        teacher, created = User.objects.get_or_create(**teacher_data)
        subject = Subject.objects.create(teacher=teacher, **validated_data)
        return subject
