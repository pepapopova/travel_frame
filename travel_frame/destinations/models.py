from django.db import models

from travel_frame.core.validators import validate_only_letters, validate_image


def max_len(choices):
    return max(len(name) for name, _ in choices)


class Country(models.Model):
    class Meta:
        verbose_name_plural = "Countries"

    COUNTRY_MAX_LENGTH = 30
    CONTINENTS = (
        ("Europe", "Europe"),
        ("North America", "North America"),
        ("South America", "South America"),
        ("Asia", "Asia"),
        ("Africa", "Africa"),
        ("Australia and Oceania", "Australia and Oceania"),
        ("Antarctica", "Antarctica")
    )

    name = models.CharField(
        max_length=COUNTRY_MAX_LENGTH,
        validators=(validate_only_letters,
                    )
    )

    continent = models.CharField(
        choices=CONTINENTS,
        max_length=max_len(CONTINENTS)
    )

    population = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    flag = models.ImageField(
        upload_to='countries_flags/',
        null=False,
        blank=True,
        validators=(validate_image,
                    )
    )

    def __str__(self):
        return self.name
