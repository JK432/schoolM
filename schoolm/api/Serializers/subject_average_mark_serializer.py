from rest_framework import serializers
from rest_framework.serializers import ValidationError


class SubjectAverageMarkSerializer(serializers.Serializer):

    subject_id = serializers.IntegerField()
    subject_name = serializers.CharField()
    average_mark = serializers.DecimalField(max_digits=5, decimal_places=2)

    def validate(self, data):
        if len(data["name"]) < 3:
            raise ValidationError("Name must have more than 3 field")
        return data
