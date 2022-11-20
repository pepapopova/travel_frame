from django.urls import path

from travel_frame.travel_photos.views import post_photo

urlpatterns = (
    path('add/', post_photo, name='post travel photo'),
)