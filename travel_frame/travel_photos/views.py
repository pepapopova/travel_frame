from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from travel_frame.travel_photos.forms import TravelPhotoPostForm


@login_required
def post_photo(request):
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