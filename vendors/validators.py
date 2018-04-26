from django.core.validators import RegexValidator, MaxLengthValidator, MaxValueValidator
from django.utils.translation import ugettext as _

phone_validator = RegexValidator(
    regex=r'(\+98|0)?9\d{9}',
    message=_("phone number must be entered in the format: '+999999999'. (up to 15 digits allowed)")
)

wallet_validator = RegexValidator(
    regex=r'^0x[a-fA-F0-9]{40}$',
    message=_('wallet id should be a valid LarinToken walletID')
)
ll_phone_validator = RegexValidator(
    regex=r'^\+?\d{9,11}$',
    message=_("your landline phone text is incorrect , please provicde a valid number up to 15digits")
)

postal_code_validator = MaxLengthValidator(
    message=_("make sure your postal code is exactly 10 digits"),
    limit_value=10
)
national_code_validator = MaxLengthValidator(
    message=_("make sure your national code is exactly 10 digits"),
    limit_value=10
)

discount_validator = MaxValueValidator(
    message=_('discount must be a number between 1 to 99'),
    limit_value=99,
)
