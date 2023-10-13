from rest_framework import serializers
from ..models import *
from .user_serializer import UserSerializer
from .subject_serializers import SubjectSerializer


class MarkSerializer(serializers.ModelSerializer):
    student = UserSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Mark
        fields = "__all__"

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        subject_data = validated_data.pop('subject')
        student, created = User.objects.get_or_create(**student_data)
        subject,created = Subject.objects.get_or_create(**subject_data)
        mark = Mark.objects.create(student=student,subject=subject **validated_data)
        return mark
