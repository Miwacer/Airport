from django.utils import timezone
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from airport.models import Flight, Airport, Route, AirplaneType, Crew, Airplane
from airport.serializers import FlightListSerializer, FlightDetailSerializer

FLIGHT_URL = reverse("airport:flight-list")

def sample_flight(**params):
    airport1, _ = Airport.objects.get_or_create(name="Kyiv Airport", closest_big_city="Kyiv")
    airport2, _ = Airport.objects.get_or_create(name="Barcelona Airport", closest_big_city="Barcelona")

    route, _ = Route.objects.get_or_create(source=airport1, destination=airport2, distance=2400)

    airplane_type, _ = AirplaneType.objects.get_or_create(name="Boeing 737")

    airplane = Airplane.objects.create(
        name="F-16",
        rows=1,
        seats_in_row=2,
        airplane_type=airplane_type
    )

    defaults = {
        "route": route,
        "airplane": airplane,
        "departure_time": timezone.now(),
        "arrival_time": timezone.now() + timedelta(hours=3),
    }
    defaults.update(params)

    flight = Flight.objects.create(**defaults)

    crew1 = Crew.objects.create(first_name="Ivan", last_name="Petrenko")
    crew2 = Crew.objects.create(first_name="Anna", last_name="Shevchenko")
    flight.crews.set([crew1, crew2])


    return flight


class UnauthorizedFlightApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        response = self.client.get(FLIGHT_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthorizedFlightApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@gmail.com",
            "testpassword123"
        )
        self.client.force_authenticate(user=self.user)

    def test_auth_required(self):
        response = self.client.get(FLIGHT_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_flight_list(self):
        sample_flight()

        response = self.client.get(FLIGHT_URL)
        flights = Flight.objects.all().order_by("id")
        serializer = FlightListSerializer(flights, many=True)

        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_flight_detail(self):
        flight = sample_flight()
        url = reverse("airport:flight-detail", args=[flight.id])

        response = self.client.get(url)
        serializer = FlightDetailSerializer(flight)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_by_route(self):
        sample_flight()

        response1 = self.client.get(FLIGHT_URL, {"route": "Kyiv"})
        response2 = self.client.get(FLIGHT_URL, {"route": "Lviv"})

        flights = Flight.objects.all()
        serializer = FlightListSerializer(flights, many=True)

        self.assertEqual(response1.data["results"], serializer.data)
        self.assertNotIn(response2.data["results"], [])
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_filter_by_departure_and_arrival_time(self):
        now = timezone.now()
        tomorrow = now + timedelta(days=1)

        sample_flight(
            departure_time=now,
            arrival_time=now + timedelta(hours=2)
        )

        sample_flight(
            departure_time=tomorrow,
            arrival_time=tomorrow + timedelta(hours=2)
        )

        response_dep = self.client.get(FLIGHT_URL, {
            "departure_time": now.strftime("%Y-%m-%d")
        })

        expected_dep = Flight.objects.filter(departure_time__date=now.date())
        serializer_dep = FlightListSerializer(expected_dep, many=True)
        self.assertEqual(response_dep.status_code, 200)
        self.assertEqual(response_dep.data["results"], serializer_dep.data)

        response_arr = self.client.get(FLIGHT_URL, {
            "arrival_time": tomorrow.strftime("%Y-%m-%d")
        })

        expected_arr = Flight.objects.filter(arrival_time__date=tomorrow.date())
        serializer_arr = FlightListSerializer(expected_arr, many=True)
        self.assertEqual(response_arr.status_code, 200)
        self.assertEqual(response_arr.data["results"], serializer_arr.data)
