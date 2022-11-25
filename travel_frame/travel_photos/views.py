from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from travel_frame.travel_photos.forms import TravelPhotoPostForm, TravelPhotoEditForm, TravelPhotoDeleteForm
from travel_frame.travel_photos.models import TravelPhoto
from travel_frame.travel_photos.utils import get_travel_photo_by_pk_and_username


@login_required
def post_travel_photo(request):

    if request.method == 'GET':
        form = TravelPhotoPostForm()
    else:
        form = TravelPhotoPostForm(request.POST, request.FILES)
        if form.is_valid():
            travel_photo = form.save(commit=False)
            travel_photo.user = request.user
            travel_photo.save()

            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(
        request,
        'travel_photos/post-travel-photo.html',
        context,
    )


def details_travel_photo(request, username, pk):
    travel_photo = get_travel_photo_by_pk_and_username(pk=pk, username=username)

    user_liked_photo = TravelPhoto.objects.filter(pk=pk, user_id=request.user.pk)

    context = {
        'travel_photo': travel_photo,
        'photo_is_liked_by_user': user_liked_photo,
        'likes_count': travel_photo.travelphotolike_set.count()
    }

    return

def edit_travel_photo(request, username, photo_id):
    travel_photo = get_travel_photo_by_pk_and_username(photo_id, username)

    if request.method == 'GET':
        form = TravelPhotoEditForm(instance=travel_photo)
    else:
        form = TravelPhotoEditForm(request.POST, request.FILES, instance=travel_photo)
        if form.is_valid():
            form.save()
            return redirect('details user', username=username)

    context = {
        'form': form,
        'photo_id': photo_id,
        'username': username
    }

    return render(
        request,
        'travel_photos/edit-travel-photo.html',
        context,
    )


def delete_travel_photo(request, username, photo_id):
    travel_photo = TravelPhoto.objects.filter(username=username, photo_id=photo_id).get()

    if request.method == 'GET':
        form = TravelPhotoDeleteForm(instance=travel_photo)
    else:
        form = TravelPhotoDeleteForm(request.POST, request.FILES, instance=travel_photo)
        if form.is_valid():
            form.save()
            return redirect('details user', username=username)

    context = {
        'form': form,
        'photo_id': photo_id,
        'username': username
    }

    return render(
        request,
        'travel_photos/delete-travel-photo.html',
        context,
    )