from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import GroupAdmin as AuthGroupAdmin, UserAdmin as AuthUserAdmin
from django.contrib.auth.models import Group, User

from vendors.models import Invoice,LarinUser,LarinCustomer,LarinVendor

class MyAdminSite(admin.AdminSite):
    site_title = _('Larin - Invoice Management Admin')
    site_header = _('Larin.cash')
    index_title = _('Invoice Management Admin')


site = MyAdminSite()

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('modified','invoice_code','vendor' ,'title', 'amount','to')
    list_filter = ('title', 'invoice_code', 'modified','vendor','to')
    search_fields = ('invoice_code', 'title')

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name','wallet_id','created','company_name','company_code','cell_phone')
    list_filter = ('name','wallet_id','created','company_name','company_code','cell_phone')
    search_fields = ('name','wallet_id','created','company_name','company_code','cell_phone')

class CustmerAdmin(admin.ModelAdmin):
    list_display = ('name','wallet_id','created')
    list_filter = ('name','wallet_id','created')
    search_fields = ('name','wallet_id','created')

site.register(LarinCustomer,CustmerAdmin)
site.register(LarinVendor,VendorAdmin)
site.register(Invoice,InvoiceAdmin)
