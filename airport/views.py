from django.shortcuts import render
from rest_framework import viewsets, mixins

from airport.models import Crew, Flight, Route, Airport, Airplane, AirplaneType
from airport.serializers import (
    FlightSerializer,
    RouteSerializer,
    AirportSerializer,
    AirplaneSerializer, AirplaneTypeSerializer, CrewListSerializer
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
    serializer_class = CrewListSerializer


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

class AirplaneViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirplaneTypeViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
