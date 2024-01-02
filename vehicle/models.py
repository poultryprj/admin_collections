from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VehicleMakeBy(models.Model):
    vehicle_make_id = models.AutoField(primary_key=True)
    vehicle_make_by = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_make_by

    class Meta:
        db_table = "VehicleMakeBy"

# Create your models here.
class VehicleModel(models.Model):
    vehicle_model_id = models.AutoField(primary_key=True)
    vehicle_model = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_model

    class Meta:
        db_table = "VehicleModel"



class VehicleType(models.Model):
    vehicle_type_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_type

    class Meta:
        db_table = "VehicleType"


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
    
    class Meta:
        db_table = "Vehicle"

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
    
    class Meta:
        db_table = "Fitness"
    
class InsuranceCompany(models.Model):
    insurance_company_id = models.AutoField(primary_key=True)
    insurance_company_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.insurance_company_name)
    
    class Meta:
        db_table = "InsuranceCompany"

    
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

    class Meta:
        db_table = "VehicleInsurance"
    

class VehiclePermit(models.Model):
    permit_id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)  #vehicle number FK of Vehicle
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

    class Meta:
        db_table = "VehiclePermit"
    

class VehiclePollution(models.Model):
    pollution_id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)  #vehicle number FK of Vehicle
    vehicle_pollution_from_Date = models.DateField()
    vehicle_pollution_to_Date = models.DateField()    
    vehicle_pollution_value = models.CharField(max_length=255)
    created_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_pollution_created_by')          #FK of User take select user
    last_modified_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_pollution_modify_by')     #FK of User update
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    lastModifiedOn = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_pollution_deleted_by')
    
    def __str__(self):
        return str(self.pollution_id)

    class Meta:
        db_table = "VehiclePollution"


class VehicleTax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)  #vehicle number FK of Vehicle
    vehicle_tax_from_Date = models.DateField()
    vehicle_tax_to_Date = models.DateField()   
    vehicle_tax_type = models.CharField(max_length=255) 
    vehicle_environment_tax = models.DecimalField(max_digits=30,decimal_places=2)
    vehicle_professional_tax = models.DecimalField(max_digits=30,decimal_places=2)
    created_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_tax_created_by')          #FK of User take select user
    last_modified_by_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_tax_modify_by')     #FK of User update
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    lastModifiedOn = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vehicle_tax_deleted_by')
    
    def __str__(self):
        return str(self.tax_id)

    class Meta:
        db_table = "VehicleTax"


class VehicleRunning(models.Model):
    vehicle_running_id = models.AutoField(primary_key=True)
    vehicleId = models.ForeignKey(Vehicle,on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(null=True)
    driverId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    kilometer = models.DecimalField(max_digits=10, decimal_places=5)
    status = models.CharField(max_length=5, null=True, blank=True)
    remark = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='VehicleRunning_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='VehicleRunning_last_modified_by')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='VehicleRunning_deleted_by')

    def __str__(self):
        return f"{self.vehicleId} - {self.datetime}"

    class Meta:
        db_table = "VehicleRunning"