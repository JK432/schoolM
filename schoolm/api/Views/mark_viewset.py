from rest_framework import viewsets
from ..models import *
from ..Serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class MarkModelViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_queryset(self):
        # return Mark.objects.filter(user=self.request.user)
        return Mark.objects.all()