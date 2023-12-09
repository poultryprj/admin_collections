from django.db import models
from django.contrib.auth.models import User
from shop.models import ProductTypes


# Create your models here.


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=250)
    vendor_code = models.CharField(max_length=100, null=True)
    vendor_type = models.CharField(max_length=250)
    vendor_company  = models.CharField(max_length=250)
    vendor_contactNo = models.CharField(max_length=15, null=True)
    vendor_alternateNo = models.CharField(max_length=15, null=True)
    vendor_address  = models.CharField(max_length=250)
    vendor_active = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Vendor_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Vendor_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Vendor_deleted')

    def __str__(self):
        return self.vendor_name
    



class VendorProduct(models.Model):
    vender_product_id = models.AutoField(primary_key=True)
    vendorId = models.ForeignKey(Vendor, on_delete=models.SET_NULL,null=True)
    productId = models.ForeignKey(ProductTypes, on_delete=models.SET_NULL,null=True)
    product_rate = models.FloatField()
    product_tcs = models.IntegerField(default=0)
    product_tds = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='VendorProduct_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='VendorProduct_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='VendorProduct_deleted')

   

