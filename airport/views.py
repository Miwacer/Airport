from django.shortcuts import render
from rest_framework import viewsets, mixins

from airport.models import Crew, Flight, Route, Airport
from airport.serializers import (
    CrewSerializer,
    FlightSerializer,
    RouteSerializer,
    AirportSerializer,
)


class AirportViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin,viewsets.GenericViewSet
):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


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


class RouteViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin ,viewsets.GenericViewSet
):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
