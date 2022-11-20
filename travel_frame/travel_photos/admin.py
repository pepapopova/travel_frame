from django.contrib import admin

from travel_frame.travel_photos.models import TravelPhoto


@admin.register(TravelPhoto)
class TravelPhotoAdmin(admin.ModelAdmin):
    pass
