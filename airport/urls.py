from django.urls import path, include
from rest_framework import routers

from airport.views import (
    CrewViewSet,
    FlightViewSet,
    RouteViewSet,
    AirportViewSet,
    AirplaneViewSet,
    AirplaneTypeViewSet,
)

router = routers.DefaultRouter()
router.register("crews", CrewViewSet)
router.register("flights", FlightViewSet)
router.register("routes", RouteViewSet)
router.register("airports", AirportViewSet)
router.register("airplanes", AirplaneViewSet)
router.register("airplane-types", AirplaneTypeViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "airport"
