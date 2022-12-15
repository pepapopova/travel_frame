from django.contrib.auth import get_user_model
from django.db import models

from travel_frame.core.validators import validate_image
from travel_frame.destinations.models import Country
from travel_frame.core.validators import validate_start_with_capital, validate_only_letters

UserModel = get_user_model()


class TravelPhoto(models.Model):
    DESCRIPTION_MAX_LENGTH = 400
    CITY_MAX_LENGTH = 30
    TAGS_MAX_LENGTH = 300

    photo = models.ImageField(
        upload_to='travel_photos/',
        validators=(validate_image,
                    )
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
    )

    date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    location = models.ForeignKey(
        Country,
        on_delete=models.RESTRICT,
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        validators=(validate_start_with_capital,
                    validate_only_letters,),
        null=True,
        blank=False,
    )

    def __str__(self):
        return f'{self.location} {self.date} {self.description}'

    class Meta:
        ordering = ('-date',)
