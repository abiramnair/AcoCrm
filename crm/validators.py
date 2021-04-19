from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def mobile_number_validator(value):
    if len(value) != 8:
        raise ValidationError(
            _('Mobile number must contain exactly 8 digits')
        )
    if not any(number.isdigit() for number in value):
        raise ValidationError(
            _('Mobile number must only contain digits.')
        )


def discount_validator(value):
    if value >= 100:
        raise ValidationError(_('Discount value cannot exceed 100%'))
