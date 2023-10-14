from django.conf import settings
from django_filters.rest_framework import FilterSet
from rest_framework import serializers
from ..models import *


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id', 'name']

