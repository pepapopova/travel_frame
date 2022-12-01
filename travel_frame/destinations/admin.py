from django.contrib import admin

from travel_frame.destinations.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "continent")
    list_filter = ('name', 'continent')
    search_fields = ('name', 'continent')