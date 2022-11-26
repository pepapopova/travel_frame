from django import forms
from django.forms import CharField, PasswordInput

from travel_frame.travel_photos.models import TravelPhoto


class TravelPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = TravelPhoto
        fields = "__all__"
        labels = {
            'photo': 'Travel Photo',
        }


class TravelPhotoPostForm(TravelPhotoBaseForm):
    class Meta:
        model = TravelPhoto
        exclude = ('date', 'user')
        labels = {
            'photo': 'Travel Photo',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Tell us more about this place?'
                })}


class TravelPhotoEditForm(TravelPhotoBaseForm):
    class Meta:
        model = TravelPhoto
        exclude = ('photo', 'date', 'user')


class TravelPhotoDeleteForm(TravelPhotoBaseForm):
    class Meta:
        model = TravelPhoto
        fields = ()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self._disable_fields()
    #     #
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
