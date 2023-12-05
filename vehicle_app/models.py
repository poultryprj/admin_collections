from django.db import models

from shop.models import ProductMaster, ProductTypes
from user.models import UserModel
from django.contrib.auth.models import User

# Create your models here.
class VehicleMakeBy(models.Model):
    vehicle_make_id = models.AutoField(primary_key=True)
    vehicle_make_by = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_make_by


# Create your models here.
class VehicleModel(models.Model):
    vehicle_model_id = models.AutoField(primary_key=True)
    vehicle_model = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_model



# Create your models here.
class VehicleType(models.Model):
    vehicle_type_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_type




class Vehicle(models.Model):
    vehicle_id  = models.AutoField(primary_key=True)
    registration_no = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=100)
    vehicle_make_Id = models.ForeignKey(VehicleMakeBy, on_delete=models.SET_NULL, null=True)
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.SET_NULL, null=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True)
    vehicle_details = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=50)
    no_of_wheel = models.IntegerField()
    carrier_type = models.CharField(max_length=100)
    registration_date = models.DateField()

    def __str__(self):
        return self.registration_no
    


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=150)
    vendor_type = models.CharField(max_length=150)

    def __str__(self):
        return self.vendor_name
    


class ProductRecieve(models.Model):
    product_record_id = models.AutoField(primary_key=True)
    recieved_date = models.DateTimeField(null=True)
    vendorId = models.ForeignKey(Vendor,on_delete=models.SET_NULL, null=True)
    product_typeId = models.ForeignKey(ProductTypes,on_delete=models.SET_NULL, null=True)
    productId = models.ForeignKey(ProductMaster,on_delete=models.SET_NULL, null=True)
    paper_rate = models.DecimalField(max_digits=10 ,decimal_places = 2)
    recieved_quantity = models.IntegerField()
    recieved_weight = models.DecimalField(max_digits=10,decimal_places=2)
    daily_rate = models.DecimalField(max_digits=10,decimal_places=2)
    tcs_rate = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    tcs_value = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    recieved_amount = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    vehicleId = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    driverId = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    source_vehicle_id = models.IntegerField()
    source_driver_id = models.IntegerField()
    challan_no = models.CharField(max_length=150)
    entry_source = models.IntegerField()
    latitude = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    longtitude = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='product_received_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='product_received_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='product_received_deleted')
    delete_reason = models.CharField(max_length=150)

    def __str__(self):
        return str(self.product_record_id)
