from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm, AuthenticationForm

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'gender', 'age')
        field_classes = {'username': UsernameField}


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': UsernameField}


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={"autofocus": True,
                   "placeholder": 'Username',
                   }))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password",
                   "placeholder": "Password"}
        )
    )
