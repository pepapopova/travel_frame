from django.shortcuts import render

from travel_frame.travel_photos.models import TravelPhoto


def index(request):
    travel_photos = TravelPhoto.objects.all()
    context = {
        "travel_photos": travel_photos
    }
    return render(request, 'common/index.html')
