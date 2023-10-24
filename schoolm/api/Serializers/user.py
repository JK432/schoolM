from rest_framework.serializers import ModelSerializer
from ..models import *
from rest_framework import serializers


class StudentSerializer(ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name','password','role']


