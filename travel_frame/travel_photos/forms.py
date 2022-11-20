from django import forms
from django.forms import CharField, PasswordInput

from travel_frame.travel_photos.models import TravelPhoto


class TravelPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = TravelPhoto
        fields = "__all__"


class TravelPhotoPostForm(TravelPhotoBaseForm):
    pass


class TravelPhotoEditForm(TravelPhotoBaseForm):
    pass


class TravelPhotoDeleteForm(TravelPhotoBaseForm):
    pass