from django.contrib import admin

from travel_frame.common.models import TravelPhotoComment, TravelPhotoSave, TravelPhotoLike


@admin.register(TravelPhotoLike)
class LikeTravelPhotoAdmin(admin.ModelAdmin):
    list_display = ('user', 'travel_photo')


@admin.register(TravelPhotoComment)
class CommentTravelPhotoAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'travel_photo')


@admin.register(TravelPhotoSave)
class SaveTravelPhotoAdmin(admin.ModelAdmin):
    list_display = ('user', 'saved_photos')

