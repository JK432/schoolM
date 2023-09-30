from rest_framework import serializers
from rest_framework.serializers import ValidationError
from ..models import Subject, Mark, User



class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = "__all__"

    def validate(self, data):
        if data["mark"] < 0:
            raise ValidationError("No negative marks")
        return data