from django.urls import path

from travel_frame.common.views import index, like_travel_photo, comment_travel_photo, save_travel_photo

urlpatterns = (
    path('', index, name='home page'),
    path('like/<int:photo_id>', like_travel_photo, name='like travel photo'),
    path('comment/<int:photo_id>/', comment_travel_photo, name='comment travel photo'),
    path('save/<int:photo_id>/', save_travel_photo, name='save travel photo'),
)