from django import forms
from django.forms import CharField, PasswordInput

from travel_frame.common.models import TravelPhotoLike, TravelPhotoComment, TravelPhotoSave
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
                }),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Where is this photo taken?'
                }
            )}


class TravelPhotoEditForm(TravelPhotoBaseForm):
    class Meta:
        model = TravelPhoto
        exclude = ('photo', 'date', 'user')


class TravelPhotoDeleteForm(TravelPhotoBaseForm):
    class Meta:
        model = TravelPhoto
        fields = ()
        disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:

            TravelPhotoLike.objects.filter(travel_photo_id=self.instance.id) \
                .delete()
            TravelPhotoComment.objects.filter(travel_photo_id=self.instance.id) \
                .delete()
            TravelPhotoSave.objects.filter(saved_photos_id=self.instance.id) \
                .delete()
            self.instance.delete()

        return self.instance
