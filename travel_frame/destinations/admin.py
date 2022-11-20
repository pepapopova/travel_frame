from django.contrib import admin

from travel_frame.destinations.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "continent")