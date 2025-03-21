from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    # list_filter = ("flights",)
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)