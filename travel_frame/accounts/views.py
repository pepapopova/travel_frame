from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from travel_frame.accounts.forms import UserCreateForm
from travel_frame.destinations.models import Country
from travel_frame.travel_photos.models import TravelPhoto

UserModel = get_user_model()


class LoginTravelView(LoginView):
    template_name = 'accounts/user-login.html'


class RegisterTravelView(generic.CreateView):
    template_name = 'accounts/user-register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home page')


class LogoutTravelView(LogoutView):
    next_page = reverse_lazy('home page')


class UserDetailsView(generic.DetailView):
    template_name = 'accounts/user-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['travel_photos'] = self.object.travelphoto_set.all()
        context['travel_photos_count'] = self.object.travelphoto_set.count()

        photos = self.object.travelphoto_set.prefetch_related('travelphotolike_set')

        context['likes_count'] = sum(x.travelphotolike_set.count() for x in photos)
        context['favourites_count'] = self.object.travelphotosave_set.count()
        context['visited_countries_count'] = self.visited_countries_count(context['travel_photos'])

        visited_countries = set(Country.objects.filter(travelphoto__user_id=self.object.pk))
        context['visited_countries'] = visited_countries

        return context

    @staticmethod
    def visited_countries_count(travel_photos):
        locations = set()
        for photo in travel_photos:
            locations.add(photo.location)
        return len(locations)


class UserEditView(generic.UpdateView):
    template_name = 'accounts/user-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender', 'age', 'profile_pic')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
             'pk': self.request.user.pk
        })


class UserDeleteView(generic.DeleteView):
    template_name = 'accounts/user-delete.html'
    model = UserModel
    success_url = reverse_lazy('home page')


class UserFavoritesView(generic.DetailView):
    template_name = 'accounts/user-favorites.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['travel_photos_count'] = self.object.travelphoto_set.count()
        context['travel_photos'] = TravelPhoto.objects.all()
        context['likes_count'] = self.object.travelphoto_set.count()
        context['saved_photos'] = TravelPhoto.objects.filter(travelphotosave__user_id=self.object.pk)
        context['favourites_count'] = self.object.travelphotosave_set.count()

        return context

