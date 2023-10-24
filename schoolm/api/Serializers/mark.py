from ..models import *
from rest_framework.serializers import ModelSerializer
from .subject import SubjectSerializer


class MarkSerializer(ModelSerializer):


    class Meta:
        model = Mark
        fields = ['id', 'mark', 'subject', 'student']
