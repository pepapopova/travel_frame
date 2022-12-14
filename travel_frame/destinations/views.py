from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from travel_frame.destinations.forms import AddCountriesForm


@login_required
def add_destination(request):

    if not request.user.is_staff:
        return redirect('home page')

    if request.method == 'GET':
        form = AddCountriesForm()
    else:
        form = AddCountriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(
        request,
        'destinations/add_destination.html',
        context,
    )