from django.urls import path
from travel_frame.destinations.views import add_destination
urlpatterns = (
    path('add/', add_destination, name='add destination'),
)
