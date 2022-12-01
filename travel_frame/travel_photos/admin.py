from django.contrib import admin

from travel_frame.travel_photos.models import TravelPhoto


@admin.register(TravelPhoto)
class TravelPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'location', 'city')
    list_filter = ('location', 'city')
    search_fields = ('location__name', 'user__username')
    fieldsets = ('Photo details',
     {'fields': ('photo', 'description')}),\
                ('User details',
     {'fields': ('user', )}), \
                ('Location details',
     {'fields': ('location', 'city')}),


    # @staticmethod
    # def tagged_users(obj):
    #     tagged_users = obj.tagged_users_set.all()
    #     if tagged_users:
    #         return ', '.join(p.username for p in tagged_users)
    #     return 'No tagged users'
