from rest_framework.serializers import ValidationError
from rest_framework import serializers
from .models import Subject, Mark, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if len(data["name"]) < 3:
            raise ValidationError("Name must have more than 3 field")
        return data


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"

    def validate(self, data):
        if len(data["name"]) < 3:
            raise ValidationError("Name must have more than 3 field")
        return data


class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = "__all__"

    def validate(self, data):
        if data["mark"] < 0:
            raise ValidationError("No negative marks")
        return data
