from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render, redirect
from travel_frame.accounts.views import RegisterTravelView
from travel_frame.common.models import TravelPhotoLike, TravelPhotoSave, TravelPhotoComment
from travel_frame.core.utils import apply_likes_count, apply_user_liked_photo, apply_user_saved_photo, get_photo_url
from travel_frame.travel_photos.models import TravelPhoto
from django.contrib.auth.decorators import login_required
from travel_frame.common.forms import SearchTravelPhotosForm, PhotoCommentForm

UserModel = get_user_model()


def index(request):

    # if not request.user.is_authenticated:
    #     return render(request, 'accounts/user-login.html')

    travel_photos = TravelPhoto.objects.all()

    search_form = SearchTravelPhotosForm(request.POST)
    searched_user = None
    if search_form.is_valid():
        searched_user = search_form.cleaned_data['searched_profile']

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
        'comment_form': PhotoCommentForm,
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
    photo = TravelPhoto.objects.filter(pk=photo_id) \
        .get()

    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.travel_photo = photo
        comment.user_id = request.user.pk
        comment.save()

    return redirect(get_photo_url(request, photo_id))


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


