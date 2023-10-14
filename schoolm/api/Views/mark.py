from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *
from django.conf import settings
from django_filters.rest_framework import FilterSet
from ..mixins.user_mixin import Role


class MarkFilter(FilterSet):
    class Meta:
        model = Mark
        fields = {
            'mark': settings.FILTER_NUMBER_MODELS,
            'subject': settings.FILTER_EXACT_MODELS,
            'student': settings.FILTER_EXACT_MODELS,
        }


class MarkModelViewSet(ModelViewSet):
    serializer_class = MarkSerializer
    filterset_class = MarkFilter

    def get_queryset(self):
        return Mark.objects.filter(student__role=Role.STUDENT)


