from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=100)
    closest_big_city = models.CharField(max_length=100, unique=True)


class Airplane(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    airplane_type = models.ForeignKey(
        "AirplaneType", on_delete=models.CASCADE, related_name="airplane"
    )


class AirplaneType(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Crew(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Route(models.Model):
    source = models.ForeignKey(
        "Airport", on_delete=models.CASCADE, related_name="departures"
    )
    destination = models.ForeignKey(
        "Airport", on_delete=models.CASCADE, related_name="arrivals"
    )
    distance = models.IntegerField()


class Flight(models.Model):
    route = models.ForeignKey("Route", on_delete=models.CASCADE, related_name="flights")
    airplane = models.ForeignKey(
        "Airplane", on_delete=models.CASCADE, related_name="flights"
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(
        "Flight", on_delete=models.CASCADE, related_name="tickets"
    )
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="tickets")


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="orders")
