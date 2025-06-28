from django.urls import path, include
from rest_framework import routers

from airport.views import CrewViewSet, FlightViewSet, RouteViewSet

router = routers.DefaultRouter()
router.register("crews", CrewViewSet)
router.register("flights", FlightViewSet)
router.register("routes", RouteViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "airport"
