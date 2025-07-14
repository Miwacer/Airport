from django.contrib import admin

from airport.models import (
    Airport,
    Airplane,
    Flight,
    AirplaneType,
    Ticket,
    Route,
    Crew,
    Order,
)

admin.site.register(Airport)
admin.site.register(Airplane)
admin.site.register(AirplaneType)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Order)
admin.site.register(Crew)
admin.site.register(Route)
