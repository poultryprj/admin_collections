from django.db import models
from django.contrib.auth.models import User
from vehicle2.models import Vendor
from django.contrib.auth.models import Group

# Create your models here.
class Assets(models.Model):
    asset_id = models.AutoField(primary_key=True)
    asset_name = models.CharField(max_length=255)
    asset_types = models.CharField(max_length=255)
    slowly_finished_product = models.CharField(max_length=255, blank=True)
    long_lasting_products = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Assets_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Assets_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Assets_deleted')

    def __str__(self):
        return str(self.asset_id)


class AssetPurchase(models.Model):
    asset_purchase_id = models.AutoField(primary_key=True)
    purchase_on = models.DateTimeField()
    vendor_Id = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)   #Vendor FK
    asset_Id = models.ForeignKey(Assets, on_delete=models.SET_NULL, null=True)   #Assets FK
    quantity = models.IntegerField()
    weight = models.DecimalField(max_digits=30,decimal_places=2)
    rate = models.DecimalField(max_digits=30,decimal_places=2)
    amount = models.DecimalField(max_digits=30,decimal_places=2)
    remarks = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='AssetsPurchase_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='AssetsPurchase_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='AssetsPurchase_deleted')

    def __str__(self):
        return str(self.asset_purchase_id)

class AssetDistribution(models.Model):
    asset_distribution_id = models.AutoField(primary_key=True)
    distribution_date_and_time = models.DateTimeField()
    assets_consumer_type = models.CharField(max_length=255)
    user_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)   #FK Group
    distribution_to_id = models.IntegerField()
    quantity = models.IntegerField()
    weight = models.DecimalField(max_digits=30,decimal_places=2)
    remarks = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='AssetsDistribution_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='AssetsDistribution_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='AssetsDistribution_deleted')

    def __str__(self):
        return str(self.asset_distribution_id)

class AssetStock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    asset_Id = models.ForeignKey(Assets, on_delete=models.SET_NULL, null=True)
    asset_stock_quantity = models.IntegerField()
    asset_stock_weight = models.DecimalField(max_digits=30,decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='AssetsStocks_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='AssetsStocks_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='AssetsStocks_deleted')

    def __str__(self):
        return str(self.stock_id)