from rest_framework import viewsets
from ..models import *
from ..serializers import *
from django.conf import settings
from django_filters.rest_framework import FilterSet


class SubjectFilter(FilterSet):
    class Meta:
        model = Subject
        fields = {
            'name': settings.FILTER_STRING_MODELS,
        }


class SubjectModelViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filterset_class = SubjectFilter
