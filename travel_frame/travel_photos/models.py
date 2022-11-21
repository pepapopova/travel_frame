from django.contrib.auth import get_user_model
from django.db import models

from travel_frame.core.validators import validate_image
from travel_frame.destinations.models import Country

UserModel = get_user_model()


class TravelPhoto(models.Model):
    DESCRIPTION_MAX_LENGTH = 400

    photo = models.ImageField(
        upload_to='travel_photos/',
        validators=(validate_image,
                    )
    )

    description = models.TextField(
        max_length= DESCRIPTION_MAX_LENGTH,
    )

    date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    tagged_users = models.ManyToManyField(
        UserModel, blank=True,
    )

    location = models.ForeignKey(
        Country,
        on_delete=models.RESTRICT,
    )