from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render, redirect

from travel_frame.accounts.views import RegisterTravelView
from travel_frame.common.models import TravelPhotoLike, TravelPhotoSave
from travel_frame.travel_photos.models import TravelPhoto
from django.contrib.auth.decorators import login_required
from travel_frame.common.forms import TravelPhotoComment, SearchTravelPhotosForm

UserModel = get_user_model()


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


def apply_likes_count(photo):
    photo.likes_count = photo.travelphotolike_set.count()
    return photo


def apply_user_liked_photo(request, photo):
    photo.is_liked_by_user = photo.travelphotolike_set.filter(user_id=request.user.pk)
    return photo


def apply_user_saved_photo(request, photo):
    photo.is_saved_by_user = photo.travelphotosave_set.filter(user_id=request.user.pk)
    return photo


def index(request):
    travel_photos = TravelPhoto.objects.all()

    search_form = SearchTravelPhotosForm(request.GET)
    searched_user = None
    if search_form.is_valid():
        searched_user = search_form.cleaned_data['username']

    if searched_user:
        travel_photos = travel_photos.filter(Q(user__username__icontains=searched_user) |
                                             Q(user__first_name__icontains=searched_user) |
                                             Q(user__last_name__icontains=searched_user))

    travel_photos = [apply_likes_count(travel_photo) for travel_photo in travel_photos]
    travel_photos = [apply_user_liked_photo(request, travel_photo) for travel_photo in travel_photos]
    travel_photos = [apply_user_saved_photo(request, travel_photo) for travel_photo in travel_photos]

    context = {
        "travel_photos": travel_photos,
        "user": UserModel,
        'comment_form': TravelPhotoComment,
        'search_form': search_form,
        'register_form': RegisterTravelView
    }

    return render(request, 'common/index.html', context)


@login_required
def like_travel_photo(request, photo_id):
    user_liked_photos = TravelPhotoLike.objects \
        .filter(travel_photo_id=photo_id, user_id=request.user.pk)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        TravelPhotoLike.objects.create(
            travel_photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(get_photo_url(request, photo_id))


@login_required
def comment_travel_photo(request, photo_id):
    photo = TravelPhoto.objects.filter(photo_id=photo_id) \
        .get()

    form = TravelPhotoComment(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)  # Does not persist to DB
        comment.photo = photo
        comment.save()

    return redirect('index')


@login_required
def save_travel_photo(request, photo_id):
    user_saved_photos = TravelPhotoSave.objects \
        .filter(saved_photos_id=photo_id, user_id=request.user.pk)

    if user_saved_photos:
        user_saved_photos.delete()
    else:
        TravelPhotoSave.objects.create(
            saved_photos_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(get_photo_url(request, photo_id))


