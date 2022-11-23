from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from travel_frame.travel_photos.forms import TravelPhotoPostForm, TravelPhotoEditForm, TravelPhotoDeleteForm
from travel_frame.travel_photos.models import TravelPhoto


@login_required
def post_travel_photo(request):

    if request.method == 'GET':
        form = TravelPhotoPostForm()
    else:
        form = TravelPhotoPostForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()

            return redirect('home page')

    context = {
        'form': form,
    }

    return render(
        request,
        'travel_photos/post-travel-photo.html',
        context,
    )

def edit_travel_photo(request, username, photo_id):
    travel_photo = TravelPhoto.objects.filter(username=username, photo_id=photo_id).get()

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