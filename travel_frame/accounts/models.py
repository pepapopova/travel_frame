from django.contrib.auth.models import AbstractUser
from django.db import models


def max_len(choices):
    return max(len(name) for name, _ in choices)


class TravelUser(AbstractUser):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    AGE_RESTRICTION = 14

    GENDER = (('male', 'male'),
              ('female', 'female'),
              ('other', 'other'))

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH
    )

    email = models.EmailField(
        unique=True
    )

    gender = models.CharField(
        choices=GENDER,
        max_length=max_len(GENDER)

    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    profile_pic = models.ImageField(
        upload_to='profile_pics',
        null=True,
        blank=True,
    )