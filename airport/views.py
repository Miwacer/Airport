from datetime import datetime

from .filters import filter_by_date

from django.db.models import Q

from rest_framework import viewsets, mixins

from airport.models import Crew, Flight, Route, Airport, Airplane, AirplaneType, Order
from airport.serializers import (
    FlightListSerializer,
    RouteSerializer,
    AirportSerializer,
    AirplaneDetailSerializer,
    CrewSerializer,
    FlightDetailSerializer,
    AirplaneTypeSerializer,
    AirplaneListSerializer,
    OrderSerializer,
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
    serializer_class = CrewSerializer


class FlightViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Flight.objects.select_related(
        "airplane", "route__source", "route__destination"
    ).prefetch_related("crews")

    @staticmethod
    def _params_to_ints(qs):
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self, departure_time=None):
        departure_time = self.request.query_params.get("departure_time")
        arrival_time = self.request.query_params.get("arrival_time")
        route = self.request.query_params.get("route")

        queryset = self.queryset

        if route:
            queryset = queryset.filter(
                Q(route__source__name__icontains=route) |
                Q(route__destination__name__icontains=route)
            )

        if departure_time:
            queryset = filter_by_date(queryset, departure_time, "departure_time")

        if arrival_time:
            queryset = filter_by_date(queryset, arrival_time, "arrival_time")

        return queryset


    def get_serializer_class(self):
        if self.action == "list":
            return FlightListSerializer

        if self.action == "retrieve":
            return FlightDetailSerializer


class RouteViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Route.objects.all().select_related("source", "destination")
    serializer_class = RouteSerializer


class AirplaneViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Airplane.objects.select_related("airplane_type")

    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneListSerializer

        if self.action == "retrieve":
            return AirplaneDetailSerializer


class AirplaneTypeViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class OrderViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = Order.objects.prefetch_related("tickets")
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
