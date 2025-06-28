from rest_framework import serializers

from airport.models import Crew, Flight


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ("full_name", )


class FlightSerializer(serializers.ModelSerializer):
    crews = CrewSerializer(many=True)

    class Meta:
        model = Flight
        fields = ("id", "route", "airplane", "departure_time", "arrival_time", "crews")
