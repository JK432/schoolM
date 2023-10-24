from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *
from django.conf import settings
from django_filters.rest_framework import FilterSet
from rest_framework.permissions import IsAuthenticated


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'email': settings.FILTER_NUMBER_MODELS,
            'first_name': settings.FILTER_EXACT_MODELS,
            'last_name': settings.FILTER_EXACT_MODELS,

        }


class UserModelViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    filterset_class = UserFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


