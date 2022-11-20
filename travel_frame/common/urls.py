from django.urls import path

from travel_frame.common.views import index

urlpatterns = (
    path('', index, name='home page'),
)