import random

import re
from decimal import Decimal

from django.utils.formats import number_format
from django.utils.translation import ngettext



def get_unique_identifier(model, field, length):
    # model = apps.get_model('shop',model_str)
    while True:

        identifier = 'SHO-' + str(random.randint(1, 99)) + str(random.randint(0, 99)) + str(random.randint(1, 99))
        kwargs = {
            field: identifier
        }
        try:
            model.objects.get(**kwargs)
        except model.DoesNotExist:
            return identifier


def generate_new_code(model, field):
    while True:
        identifier = 'LARIN-' + str(model.objects.count()) + str(random.randint(1, 99))
        kwargs = {
            field: identifier
        }
        try:
            model.objects.get(**kwargs)
        except model.DoesNotExist:
            return identifier


def generate_withprefix_code(model, prefix, field, add_extra=True):
    while True:
        fullcode = prefix + str(model.objects.count())
        if add_extra:
            fullcode += str(random.randint(1, 999))
        kwargs = {
            field: fullcode
        }
        try:
            model.objects.get(**kwargs)
        except model.DoesNotExist:
            return fullcode

def monify(value, use_l10n=False):
    """
    Convert an integer to a string containing commas every three digits.
    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.
    """
    if settings.USE_L10N and use_l10n:
        try:
            if not isinstance(value, (float, Decimal)):
                value = int(value)
        except (TypeError, ValueError):
            return monify(value, False)
        else:
            return number_format(value, force_grouping=True)
    orig = str(value)
    new = re.sub(r"^(-?\d+)(\d{3})", r'\g<1>,\g<2>', orig)
    if orig == new:
        return new
    else:
        return monify(new, use_l10n)


# A tuple of standard large number to their converters
intword_converters = (
    (6, lambda number: (
        ngettext('%(value).1f million', '%(value).1f million', number),
        ngettext('%(value)s million', '%(value)s million', number),
    )),
    (9, lambda number: (
        ngettext('%(value).1f billion', '%(value).1f billion', number),
        ngettext('%(value)s billion', '%(value)s billion', number),
    )),
    (12, lambda number: (
        ngettext('%(value).1f trillion', '%(value).1f trillion', number),
        ngettext('%(value)s trillion', '%(value)s trillion', number),
    )),
    (15, lambda number: (
        ngettext('%(value).1f quadrillion', '%(value).1f quadrillion', number),
        ngettext('%(value)s quadrillion', '%(value)s quadrillion', number),
    )),
    (18, lambda number: (
        ngettext('%(value).1f quintillion', '%(value).1f quintillion', number),
        ngettext('%(value)s quintillion', '%(value)s quintillion', number),
    )),
    (21, lambda number: (
        ngettext('%(value).1f sextillion', '%(value).1f sextillion', number),
        ngettext('%(value)s sextillion', '%(value)s sextillion', number),
    )),
    (24, lambda number: (
        ngettext('%(value).1f septillion', '%(value).1f septillion', number),
        ngettext('%(value)s septillion', '%(value)s septillion', number),
    )),
    (27, lambda number: (
        ngettext('%(value).1f octillion', '%(value).1f octillion', number),
        ngettext('%(value)s octillion', '%(value)s octillion', number),
    )),
    (30, lambda number: (
        ngettext('%(value).1f nonillion', '%(value).1f nonillion', number),
        ngettext('%(value)s nonillion', '%(value)s nonillion', number),
    )),
    (33, lambda number: (
        ngettext('%(value).1f decillion', '%(value).1f decillion', number),
        ngettext('%(value)s decillion', '%(value)s decillion', number),
    )),
    (100, lambda number: (
        ngettext('%(value).1f googol', '%(value).1f googol', number),
        ngettext('%(value)s googol', '%(value)s googol', number),
    )),
)

