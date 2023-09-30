from rest_framework import serializers
from rest_framework.serializers import ValidationError
from ..models import Subject, Mark, User


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"

    def validate(self, data):
        if len(data["name"]) < 3:
            raise ValidationError("Name must have more than 3 field")
        return data
