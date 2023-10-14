from rest_framework.serializers import ModelSerializer
from ..models import *


class StudentSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']


