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
        return str(self.vehicle_id)
    


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=150)
    vendor_type = models.CharField(max_length=150)

    def __str__(self):
        return self.vendor_name
    


class ProductRecieve(models.Model):
    product_record_id = models.AutoField(primary_key=True)
    recieved_date = models.DateField(null=True)
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
    latitude = models.DecimalField(max_digits=20, decimal_places=5,null=True)
    longtitude = models.DecimalField(max_digits=20, decimal_places=5,null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='product_received_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='product_received_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='product_received_deleted')
    delete_reason = models.CharField(max_length=150)

    def __str__(self):
        return str(self.product_record_id)

class Fitness(models.Model):
    fitness_id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)  #vehicle number FK of Vehicle
    vehicle_fitness_from_date = models.DateField()
    vehicle_fitness_to_date = models.DateField()
    created_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_fitness_created_by')          #FK of User take select user
    last_modified_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_fitness_modify_by')     #FK of User update
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='fitness_details_deleted_by')
    last_modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fitness_id)
    
class InsuranceCompany(models.Model):
    insurance_company_id = models.AutoField(primary_key=True)
    insurance_company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.insurance_company_id

    
class VehicleInsurance(models.Model):
    insurance_id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)  #vehicle number FK of Vehicle
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.SET_NULL, null=True)   #FK company Type
    insurance_from_date = models.DateField()
    insurance_to_date = models.DateField()
    insurance_amount = models.DecimalField(max_digits=30,decimal_places=2)
    insurance_paid_amount = models.DecimalField(max_digits=30,decimal_places=2)
    created_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_insurance_created_by')          #FK of User take select user
    last_modified_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_insurance_modify_by')     #FK of User update
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_insurance_details_deleted_by')

    def __str__(self):
        return str(self.insurance_id)
    

class VehiclePermit(models.Model):
    permit_id = models.AutoField(primary_key=True)
    vehicle_permit_from_Date = models.DateField()
    vehicle_permit_to_Date = models.DateField()
    vehicle_permit_type = models.CharField(max_length=255)
    vehicle_permit_id = models.IntegerField()
    created_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_permit_created_by')          #FK of User take select user
    last_modified_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_permit_modify_by')     #FK of User update
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    lastModifiedOn = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_permit_deleted_by')
    
    def __str__(self):
        return str(self.permit_id)
