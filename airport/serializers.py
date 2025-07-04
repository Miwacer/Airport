from django.db import transaction
from rest_framework import serializers

from airport.models import (
    Crew,
    Flight,
    Route,
    Airport,
    Airplane,
    AirplaneType,
    Order,
    Ticket,
)


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ("id", "name", "closest_big_city")


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ("id", "name")


class AirplaneTypeNameSerializer(AirplaneTypeSerializer):
    class Meta:
        model = AirplaneType
        fields = ("name",)


class AirplaneListSerializer(serializers.ModelSerializer):
    airplane_type = serializers.CharField(source="airplane_type.name", read_only=True)

    class Meta:
        model = Airplane
        fields = ("id", "name", "rows", "seats_in_row", "airplane_type")


class AirplaneDetailSerializer(serializers.ModelSerializer):
    airplane_type = AirplaneTypeSerializer(read_only=True)

    class Meta:
        model = Airplane
        fields = ("id", "name", "rows", "seats_in_row", "airplane_type")


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class RouteSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="source.name", read_only=True)
    source_closest_big_city = serializers.CharField(
        source="source.closest_big_city", read_only=True
    )
    destination = serializers.CharField(source="destination.name", read_only=True)
    destination_closest_big_city = serializers.CharField(
        source="destination.closest_big_city", read_only=True
    )

    class Meta:
        model = Route
        fields = (
            "id",
            "source",
            "source_closest_big_city",
            "destination",
            "destination_closest_big_city",
            "distance",
        )


class FlightListSerializer(serializers.ModelSerializer):
    airplane = serializers.CharField(source="airplane.name", read_only=True)
    crews = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="full_name"
    )
    route = serializers.SlugRelatedField(read_only=True, slug_field="full_route")
    tickets_available = serializers.ReadOnlyField()

    class Meta:
        model = Flight
        fields = (
            "id",
            "airplane",
            "route",
            "departure_time",
            "arrival_time",
            "tickets_available",
            "crews",
        )


class TicketSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super(TicketSerializer, self).validate(attrs)
        Ticket.validate_seat(
            attrs["seat"],
            attrs["flight"].airplane.seats_in_row,
            serializers.ValidationError,
        )
        return data

    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "flight")


class TicketSeatsSerializer(TicketSerializer):
    class Meta:
        model = Ticket
        fields = ("row", "seat")


class FlightDetailSerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)
    crews = CrewSerializer(many=True, read_only=True)
    airplane = AirplaneDetailSerializer(read_only=True)
    taken_seats = TicketSeatsSerializer(source="tickets", read_only=True, many=True)

    class Meta:
        model = Flight
        fields = (
            "id",
            "airplane",
            "route",
            "taken_seats",
            "crews",
            "departure_time",
            "arrival_time",
        )


class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_null=True)

    class Meta:
        model = Order
        fields = ("id", "tickets", "created_at")

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            order = Order.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(order=order, **ticket_data)
            return order
