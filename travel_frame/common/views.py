from django.shortcuts import render, redirect

from travel_frame.common.models import TravelPhotoLike
from travel_frame.travel_photos.models import TravelPhoto


def index(request):
    travel_photos = TravelPhoto.objects.all()
    context = {
        "travel_photos": travel_photos
    }
    return render(request, 'common/index.html', context)

def like_travel_photo(request, photo_id):
    TravelPhotoLike.objects.create(photo_id=photo_id)
    return redirect('home page')