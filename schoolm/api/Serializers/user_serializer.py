from rest_framework.serializers import ValidationError
from rest_framework import serializers
from ..models import Subject, Mark, User
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if not re.fullmatch(regex, data["email"]):
            raise ValidationError("Email must be valid")
        return data
