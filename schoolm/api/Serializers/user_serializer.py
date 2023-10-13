from rest_framework import serializers
from ..models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'roles', 'email', 'password']

    password = serializers.CharField(write_only=True, required=True, max_length=128, style={'input_type': 'password'})

