from django.shortcuts import render, redirect

from travel_frame.common.models import TravelPhotoLike, TravelPhotoSave
from travel_frame.travel_photos.models import TravelPhoto
from django.contrib.auth.decorators import login_required
from travel_frame.common.forms import TravelPhotoComment


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


def index(request):
    travel_photos = TravelPhoto.objects.all()
    context = {
        "travel_photos": travel_photos
    }
    return render(request, 'common/index.html', context)


@login_required
def like_travel_photo(request, photo_id):
    user_liked_photos = TravelPhotoLike.objects \
        .filter(photo_id=photo_id, user_id=request.user.pk)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        TravelPhotoLike.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(get_photo_url(request, photo_id))

@login_required
def comment_travel_photo(request, photo_id):
    photo = TravelPhoto.objects.filter(pk=photo_id) \
        .get()

    form = TravelPhotoComment(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)  # Does not persist to DB
        comment.photo = photo
        comment.save()

    return redirect('index')


@login_required
def save_travel_photo(request, photo_id):
    user_saved_photo = TravelPhotoLike.objects \
        .filter(photo_id=photo_id)

    if request.user != user_saved_photo.tagged_user and user_saved_photo:
        TravelPhotoSave.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )
    else:
        user_saved_photo.delete()

    return redirect(get_photo_url(request, photo_id))
