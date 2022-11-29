from django.urls import path

from travel_frame.travel_photos.views import post_travel_photo, edit_travel_photo, delete_travel_photo, \
    details_travel_photo

urlpatterns = (
    path('post/', post_travel_photo, name='post travel photo'),
    path('edit/<int:pk>/', edit_travel_photo, name='edit travel photo'),
    path('delete/<int:pk>/', delete_travel_photo, name='delete travel photo'),
    path('details/<int:pk>/', details_travel_photo, name='details travel photo'),
)