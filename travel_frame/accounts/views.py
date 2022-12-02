from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from travel_frame.accounts.forms import UserCreateForm, LoginForm
from travel_frame.accounts.mixins import OnlyOwnerAccessibleMixin
from travel_frame.accounts.models import TravelUser
from travel_frame.destinations.models import Country
from travel_frame.travel_photos.models import TravelPhoto

UserModel = get_user_model()


class LoginTravelView(LoginView):
    template_name = 'accounts/user-login.html'
    form_class = LoginForm


class RegisterTravelView(generic.CreateView):
    template_name = 'accounts/user-register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home page')

class LogoutTravelView(LogoutView):
    next_page = reverse_lazy('home page')


class UserDetailsView(LoginRequiredMixin, generic.DetailView):
    template_name = 'accounts/user-details.html'
    model = UserModel
    login_url = reverse_lazy('login user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['travel_photos'] = self.object.travelphoto_set.all()
        context['travel_photos_count'] = self.object.travelphoto_set.count()

        photos = self.object.travelphoto_set.prefetch_related('travelphotolike_set')
        context['likes_count'] = sum(x.travelphotolike_set.count() for x in photos)

        context['favourites_count'] = self.object.travelphotosave_set.count()

        visited_countries = set(Country.objects.filter(travelphoto__user_id=self.object.pk))
        context['visited_countries'] = visited_countries
        context['visited_countries_count'] = len(visited_countries)

        return context

    @staticmethod
    def visited_countries_count(travel_photos):
        locations = set()
        for photo in travel_photos:
            locations.add(photo.location)
        return len(locations)


class UserEditView(OnlyOwnerAccessibleMixin, LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/user-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender', 'age', 'profile_pic')
    login_url = reverse_lazy('login user')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
             'pk': self.request.user.pk
        })


class UserDeleteView(OnlyOwnerAccessibleMixin, LoginRequiredMixin, generic.DeleteView):
    template_name = 'accounts/user-delete.html'
    model = UserModel
    success_url = reverse_lazy('home page')
    login_url = reverse_lazy('login user')


class UserFavoritesView(OnlyOwnerAccessibleMixin, LoginRequiredMixin, generic.DetailView):
    template_name = 'accounts/user-favorites.html'
    model = UserModel
    login_url = reverse_lazy('login user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['travel_photos_count'] = self.object.travelphoto_set.count()
        context['travel_photos'] = TravelPhoto.objects.all()
        context['likes_count'] = self.object.travelphoto_set.count()
        context['saved_photos'] = TravelPhoto.objects.filter(travelphotosave__user_id=self.object.pk)
        context['favourites_count'] = self.object.travelphotosave_set.count()

        return context

