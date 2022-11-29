from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from travel_frame.common.models import TravelPhotoLike
from travel_frame.core.utils import is_owner
from travel_frame.travel_photos.forms import TravelPhotoPostForm, TravelPhotoEditForm, TravelPhotoDeleteForm
from travel_frame.travel_photos.models import TravelPhoto

UserModel = get_user_model()


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


@login_required
def details_travel_photo(request, pk):
    travel_photo = TravelPhoto.objects.filter(pk=pk).get()

    user_liked_photo = TravelPhotoLike.objects.filter(travel_photo_id=pk, user_id=request.user.pk)

    context = {
        'photo': travel_photo,
        'photo_is_liked_by_user': user_liked_photo,
        'likes_count': travel_photo.travelphotolike_set.count(),
        'is_owner': request.user == travel_photo.user,
    }

    return render(request, 'travel_photos/details-travel-photo.html', context)


@login_required
def edit_travel_photo(request, pk):
    travel_photo = TravelPhoto.objects.filter(pk=pk).get()

    if not is_owner(request, travel_photo):
        return redirect('details travel photo', pk=travel_photo.pk)

    if request.method == 'GET':
        form = TravelPhotoEditForm(instance=travel_photo)
    else:
        form = TravelPhotoEditForm(request.POST, request.FILES, instance=travel_photo)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
        'photo_id': pk,
        'username': request.user.username
    }

    return render(
        request,
        'travel_photos/edit-travel-photo.html',
        context,
    )


@login_required
def delete_travel_photo(request, pk):
    travel_photo = TravelPhoto.objects.filter(pk=pk).get()

    if not is_owner(request, travel_photo):
        return redirect('details travel photo', pk=travel_photo.pk)

    if request.method == 'GET':
        form = TravelPhotoDeleteForm(instance=travel_photo)
    else:
        form = TravelPhotoDeleteForm(request.POST, request.FILES, instance=travel_photo)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
        'photo_id': pk,
        'username': request.user.username
    }

    return render(
        request,
        'travel_photos/delete-travel-photo.html',
        context,
    )