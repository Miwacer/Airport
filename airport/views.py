from django.shortcuts import render
from rest_framework import viewsets, mixins

from airport.models import Crew
from airport.serializers import (
    CrewSerializer,
)


class CrewViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
