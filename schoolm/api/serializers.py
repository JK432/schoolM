from rest_framework import serializers
from rest_framework.serializers import ValidationError
from . import models
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"

    def validate(self, data):
        if len(data["name"])<3:
            raise ValidationError("Name must have more than 3 field")
        return data


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = "__all__"

    def validate(self, data):
        if len(data["name"])<3:
            raise ValidationError("Name must have more than 3 field")
        return data


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = "__all__"

    def validate(self, data):
        if len(data["name"])<3:
            raise ValidationError("Name must have more than 3 field")
        return data


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mark
        fields = "__all__"

    def validate(self, data):
        if data["mark"]<0:
            raise ValidationError("No negative marks")
        return data


class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2')

  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user