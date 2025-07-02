from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, generics

from airport.models import (
    Crew,
    Flight,
    Route,
    Airport,
    Airplane,
    AirplaneType
)

from airport.serializers import (
    FlightListSerializer,
    RouteSerializer,
    AirportSerializer,
    AirplaneDetailSerializer,
    CrewListSerializer,
    FlightDetailSerializer,
    AirplaneTypeListSerializer,
    AirplaneListSerializer,
)


class AirportViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
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

    def get_serializer_class(self):
        if self.action == "list":
            return FlightListSerializer

        if self.action == "retrieve":
            return FlightDetailSerializer


class RouteViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class AirplaneViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Airplane.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneListSerializer

        if self.action == "retrieve":
            return AirplaneDetailSerializer


class AirplaneTypeViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeListSerializer
