from rest_framework import viewsets
from ..models import *
from ..Serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]

