from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.

## We can customize the admin feature... with what columns we want to display.
## Here, we want to see more info about the flights...
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights", )

admin.site.register(Airport)
# Register the flight with FlightAdming settings...
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
