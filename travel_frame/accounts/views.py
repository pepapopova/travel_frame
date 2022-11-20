from django.contrib.auth import views, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from travel_frame.accounts.forms import UserCreateForm

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

        return context


class UserEditView(generic.UpdateView):
    template_name = 'accounts/user-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender', 'age')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
             'pk': self.request.user.pk
        })


class UserDeleteView(generic.DeleteView):
    template_name = 'accounts/user-delete.html'
    model = UserModel
    success_url = reverse_lazy('home page')