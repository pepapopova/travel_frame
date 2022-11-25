from django.contrib import admin

from travel_frame.travel_photos.models import TravelPhoto


@admin.register(TravelPhoto)
class TravelPhotoAdmin(admin.ModelAdmin):
    list_display = ('location', 'date', 'user')

    @staticmethod
    def tagged_users(obj):
        tagged_users = obj.tagged_users_set.all()
        if tagged_users:
            return ', '.join(p.username for p in tagged_users)
        return 'No tagged users'
