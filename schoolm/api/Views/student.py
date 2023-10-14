from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *
from django_filters.rest_framework import *
from django.conf import settings
from ..mixins.user_mixin import Role


class StudentFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'email': settings.FILTER_STRING_MODELS,
            'first_name': settings.FILTER_STRING_MODELS,
            'last_name': settings.FILTER_STRING_MODELS,
        }


class StudentModelViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    filterset_class = StudentFilter

    def get_queryset(self):
        return User.objects.filter(role=Role.STUDENT)

