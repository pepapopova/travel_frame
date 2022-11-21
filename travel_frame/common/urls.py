from django.urls import path

from travel_frame.common.views import index, like_travel_photo

urlpatterns = (
    path('', index, name='home page'),
    path('travelphoto_like', like_travel_photo, name='like travel photo')
)