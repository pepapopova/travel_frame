from django.contrib import admin

from travel_frame.common.models import TravelPhotoComment, TravelPhotoSave


@admin.register(TravelPhotoComment)
class CommentTravelPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(TravelPhotoSave)
class SaveTravelPhotoAdmin(admin.ModelAdmin):
    pass

