from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from vendors.validators import phone_validator,wallet_validator,national_code_validator,ll_phone_validator
from vendors.utils import generate_new_code


def gen_invoice_id():
    return generate_new_code(Invoice, 'invoice_code')


class DateTimeAwareModel(models.Model):
    created = models.DateTimeField(
        verbose_name=_('created'),
        help_text=_('creation datetime of the object'),
        auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name=_('modified'),
        help_text=_('modification datetime of the object'),
        auto_now=True
    )

    def timestmp(self):
        return self.created.timestamp()

    def m_timestmp(self):
        return self.created.timestamp()

    class Meta:
        abstract = True


class LarinUser(DateTimeAwareModel):
    name = models.CharField(
        verbose_name=_('Larin User'),
        help_text=_('Larin User'),
        max_length=255
    )

    wallet_id = models.CharField(
        verbose_name=_('wallet id'),
        help_text=_('ethereum network valid id'),
        validators=[wallet_validator, ],
        max_length=100
    )

    def __str__(self):
        return '{title}'.format(title=self.wallet_id)



class LarinCustomer(LarinUser):
    details = models.TextField(
        verbose_name=_('Details'),
        help_text=_('informations'),
        default='-',
        blank=True,

    )

    def __str__(self):
        return '{title}'.format(title=self.name)

    class Meta:
        verbose_name = _('Larin Customer')
        verbose_name_plural = _('Larin Customers')


class LarinVendor(LarinUser):
    full_name = models.CharField(
        verbose_name=_('first name'),
        help_text=_('first name of the transferee'),
        max_length=255
    )

    company_name = models.CharField(
        verbose_name=_("Company Name"),
        help_text=_("Fill the title of your Company"),
        max_length=255
    )
    company_code = models.CharField(
        verbose_name=_("Company Code"),
        help_text=_("Enter the economic code of your Company"),
        max_length=255
    )

    national_code = models.CharField(
        verbose_name=_('national code'),
        help_text=_('national code of the transferee'),
        max_length=10,
        validators=[national_code_validator]

    )
    company_mail = models.EmailField(
        verbose_name=_("Company Mail"),
        help_text=_("enter your Comapany Mail")
    )

    cell_phone = models.CharField(
        verbose_name=_('cell phone'),
        help_text=_('cell phone number of the transferee'),
        max_length=20,
        validators=[phone_validator]
    )

    def __str__(self):
        return '{title}'.format(title=self.company_name)

    class Meta:
        verbose_name = _('Larin Vendor')
        verbose_name_plural = _('Larin Vendor')


class Invoice(DateTimeAwareModel):
    title = models.CharField(
        verbose_name=_('title'),
        help_text=_('title of the tag'),
        max_length=255
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Core Details of invoice'),
        default='-'
    )
    invoice_code = models.CharField(
        verbose_name=_('Invoice Code'),
        help_text=_('A unique code for this invoice'),
        max_length=16,
        editable=False,
        unique=True,
        default=gen_invoice_id,
    )

    vendor = models.ForeignKey(
        verbose_name=_('Vendor'),
        help_text=_('Vendor who created this invoice'),
        to=LarinVendor,
        related_name='vendor_invoices',
        on_delete=models.CASCADE

    )
    owner = models.ForeignKey(
        verbose_name=_('Owner'),
        help_text=_('owner of contract'),
        to=LarinUser,
        related_name='invoices',
        on_delete=models.CASCADE,

    )

    to = models.ForeignKey(
        verbose_name=_('Customer'),
        help_text=_('Customer who needs to pay the bill'),
        to=LarinCustomer,
        related_name='customer_invoices',
        on_delete=models.CASCADE

    )

    amount = models.IntegerField(
        verbose_name=_('Amount in Rials'),
        help_text=_('amount of contract')
    )

    phone = models.CharField(
        verbose_name=_('phone'),
        help_text=_('phone number of the transferee'),
        max_length=20,
        validators=[ll_phone_validator]
    )

    def __str__(self):
        return '{title}'.format(title=self.title)

    class Meta:
        verbose_name = _('invoice')
        verbose_name_plural = _('invoice')
