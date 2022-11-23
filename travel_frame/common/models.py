from django.contrib.auth import get_user_model
from django.db import models

from travel_frame.travel_photos.models import TravelPhoto

UserModel = get_user_model()


class TravelPhotoLike(models.Model):

    travel_photo = models.ForeignKey(
        TravelPhoto,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class TravelPhotoComment(models.Model):
    MAX_COMMENT_LENGTH = 200
    comment = models.CharField(
        max_length=MAX_COMMENT_LENGTH,
    )

    date_and_time = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=True,
    )

    travel_photo = models.ForeignKey(
        TravelPhoto,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class TravelPhotoSave(models.Model):
    class Meta:
        verbose_name_plural = "Travel Photos Save"

    saved_photos = models.ForeignKey(
        TravelPhoto,
        on_delete=models.RESTRICT,
        null=False,
        blank=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        null=False,
        blank=True
    )