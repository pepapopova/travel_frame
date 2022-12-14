from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Field must contain only letters!')


def validate_start_with_capital(value):
    if not value[0].isupper():
        raise ValidationError('Field should start with capital letter!')

def validate_image(value):
    filesize = value.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
