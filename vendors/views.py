from django.shortcuts import render
from django.shortcuts import render
from rest_framework import serializers, filters
from rest_framework import generics
from rest_framework.mixins import UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from vendors.models import LarinCustomer,LarinVendor,Invoice
# Create your views here.
import django_filters
class InvoiceSerializer(serializers.ModelSerializer):
    #TODO : add filter for owner and two by wallet id
    owner_wallet = serializers.CharField(source="owner.wallet_id")
    customer_wallet = serializers.CharField(source="to.wallet_id")
    vendor_wallet = serializers.CharField(source="vendor.wallet_id")

    def get_wallet(self, wallet):
        cars_queryset = Invoice.objects.all().filter(to__wallet_id=wallet).select_related()
        serializer = InvoiceSerializer(instance=cars_queryset, many=False, context=self.context)
        return serializer.data

    class Meta:
        model = Invoice
        fields = ('owner_wallet','customer_wallet','vendor_wallet','title','description','invoice_code','amount','phone',)
        read_only_fields = ('owner_wallet','customer_wallet','vendor_wallet',)




class InvoiceList(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('invoice_code','vendor')
    #filter_backends = (filters.BaseFilterBackend, filters.SearchFilter,)
    pagination_class = LimitOffsetPagination
    search_fields = ('invoice_code', 'vendor','owner','to')
    ordering = ('-modified',)

class InvoiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer