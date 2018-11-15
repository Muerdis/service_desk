from django.core.exceptions import ValidationError


def validate_phone(phone):
    phone = ''.join(x for x in phone if x.isdigit())

    if not len(phone) == 10:
        raise ValidationError('Мобильный телефон должен содержать 10 символов.')