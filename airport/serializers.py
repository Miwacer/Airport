from rest_framework import serializers

from airport.models import Crew, Flight, Route, Airport, Airplane, AirplaneType


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ("id", "name", "closest_big_city")


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ("id", "name", "rows", "seats_in_row", "airplane_type")


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ("id", "name")


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ("full_name", )


class FlightSerializer(serializers.ModelSerializer):
    crews = CrewSerializer(many=True)

    class Meta:
        model = Flight
        fields = ("id", "route", "airplane", "departure_time", "arrival_time", "crews")


class RouteSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="source.name", read_only=True)
    source_closest_big_city = serializers.CharField(source="source.closest_big_city", read_only=True)
    destination = serializers.CharField(source="destination.name", read_only=True)
    destination_closest_big_city = serializers.CharField(source="destination.closest_big_city", read_only=True)

    class Meta:
        model = Route
        fields = (
            "id",
            "source",
            "source_closest_big_city",
            "destination",
            "destination_closest_big_city",
            "distance"
        )
