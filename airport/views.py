from django.shortcuts import render
from rest_framework import viewsets, mixins

from airport.models import Crew, Flight
from airport.serializers import (
    CrewSerializer,
    FlightSerializer,
)


class CrewViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class FlightViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
