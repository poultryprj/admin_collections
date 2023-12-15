from django.db import models
from shops1.models import ShopModel
from django.contrib.auth.models import User

# Create your models here.

class Collection(models.Model):
    collection_id =  models.AutoField(primary_key=True)
    collection_date = models.DateField(null=True)
    collection_time = models.TimeField(null=True)
    shopId = models.ForeignKey(ShopModel, on_delete=models.SET_NULL, null=True)
    cashierId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='collection_cashier_id')
    latitude = models.DecimalField(max_digits=20, decimal_places=5,null=True)
    longtitude = models.DecimalField(max_digits=20, decimal_places=5,null=True)
    total_amount = models.FloatField()
    fanialize_on = models.DateTimeField(auto_now=True)
    fanialize_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



class CollectionMode(models.Model):
    collection_mode_id = models.AutoField(primary_key=True)
    collectionId = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)
    payment_mode = models.CharField(max_length=100)
    payment_amount = models.FloatField()
    upload_image = models.FileField(blank=True, null=True, upload_to=f's3://kukudku/collection', max_length=2000)



class SkipShop(models.Model):
    skip_shop_id = models.AutoField(primary_key=True)
    skip_shop_date = models.DateField(null=True)
    skip_shop_time = models.TimeField(null=True)
    shopId = models.ForeignKey(ShopModel, on_delete=models.SET_NULL, null=True)
    cashierId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  related_name='SkipShop_cashier_Id')
    approve_yn = models.CharField(max_length=50)
    remark = models.TextField(null=True)
    approve_byId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='SkipShop_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='SkipShop_last_modified_by')