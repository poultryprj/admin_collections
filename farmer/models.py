# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.






# # CREATE TABLE `tblFarmerInfo` (
# #   `farmerId` int NOT NULL,
# #   `farmerCode` int NOT NULL,
# #   `poultryName` varchar(255) NOT NULL,
# #   `farmerName` varchar(255) NOT NULL,
# #   `farmerAddress` varchar(255) NOT NULL,
# #   `poultryContacts` text NOT NULL,
# #   `altContact` text NOT NULL,
# #   `tcs` int NOT NULL DEFAULT '0',
# #   `tds` int NOT NULL DEFAULT '0',
# #   `boilerRate` float NOT NULL,
# #   `largeBoilerRate` float NOT NULL,
# #   `eggsRate` float NOT NULL,
# #   `gavranRate` float NOT NULL,
# #   `chickType` varchar(150) NOT NULL,
# #   `active` varchar(100) NOT NULL,
# #   `createdById` smallint NOT NULL,
# #   `lastModifiedById` smallint NOT NULL,
# #   `createdon` int NOT NULL,
# #   `lastModifiedOn` int NOT NULL,
# #   `isDeleted` int NOT NULL DEFAULT '0'
# # ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


# class FarmerModel(models.Model):
#     farmer_id = models.AutoField(primary_key=True)
#     farmer_code = models.IntegerField()
#     poultry_name = models.CharField(max_length=255)
#     farmer_name = models.CharField(max_length=255)
#     farmer_address = models.CharField(max_length=255)
#     poultry_contactNo = models.CharField(max_length=15, null=True)
#     poultry_alternateNo = models.CharField(max_length=15, null=True)
#     tcs = models.IntegerField(default=0)
#     tds = models.IntegerField(default=0)
#     boiler_rate = models.FloatField()
#     large_boiler_rate = models.FloatField()
#     eggs_rate = models.FloatField()
#     gavran_rate = models.FloatField()
#     chick_type = models.CharField(max_length=150)
#     active = models.CharField(max_length=100)
#     created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FarmerModel_created_by')
#     last_modified_on = models.DateTimeField(auto_now=True)
#     last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FarmerModel_last_modified')
#     is_deleted = models.BooleanField(default=False)
#     deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FarmerModel_deleted')



# # CREATE TABLE `tblFarmerOpeningBalance` (
# #   `id` int NOT NULL,
# #   `farmerId` int NOT NULL,
# #   `balanceDate` varchar(10) NOT NULL,
# #   `balance` float NOT NULL,
# #   `active` int NOT NULL,
# #   `adjustmentAmount` float NOT NULL,
# #   `adjustmentRemark` text NOT NULL,
# #   `balanceUTCDate` int NOT NULL,
# #   `createdById` int NOT NULL,
# #   `lastModifiedById` int NOT NULL,
# #   `createdOn` int NOT NULL,
# #   `lastModifiedOn` int NOT NULL
# # ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


# class FarmerOpeningBalance(models.Model):
#     farmer_opening_balance_id = models.AutoField(primary_key=True)
#     farmerId = models.ForeignKey(FarmerModel, on_delete=models.SET_NULL)
#     balance_date = models.DateField(max_length=10)
#     balance = models.FloatField()
#     active = models.CharField(max_length=100)
#     adjustment_amount = models.FloatField()
#     adjustment_remark = models.TextField()
#     balance_utc_date = models.DateField(auto_now_add=True)
#     created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FarmerOpeningBalance_created_by')
#     last_modified_on = models.DateTimeField(auto_now=True)
#     last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FarmerOpeningBalance_last_modified')
#     is_deleted = models.BooleanField(default=False)
#     deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FarmerOpeningBalance_deleted')





# # CREATE TABLE `tblFarmerProducts` (
# #   `id` int NOT NULL,
# #   `farmerId` int NOT NULL,
# #   `productTypeId` int NOT NULL,
# #   `productRate` float NOT NULL,
# #   `CreatedBy` int NOT NULL,
# #   `CreatedOn` int NOT NULL,
# #   `LastModifiedOn` int NOT NULL,
# #   `LastModifiedBy` int NOT NULL
# # ) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# class FarmerProducts(models.Model):
#     farmer_products_id = models.AutoField(primary_key=True)
#     farmerId = models.ForeignKey(FarmerModel, on_delete=models.SET_NULL)
#     productTypeId = models.IntegerField() # Fk or Not
#     product_rate = models.FloatField()
#     created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FarmerProducts_created_by')
#     last_modified_on = models.DateTimeField(auto_now=True)
#     last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FarmerProducts_last_modified')
#     is_deleted = models.BooleanField(default=False)
#     deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FarmerProducts_deleted')



# # CREATE TABLE `tblFarmerCreditBalance` (
# #   `id` int NOT NULL,
# #   `farmerCode` int NOT NULL,
# #   `Amount` float NOT NULL,
# #   `Reason` varchar(100) NOT NULL,
# #   `CreditDate` int NOT NULL,
# #   `isDeleted` int NOT NULL
# # ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


# class FarmerCreditBalance(models.Model):
#     farmer_credit_balance_id = models.AutoField(primary_key=True)
#     farmer_code = models.IntegerField()
#     amount = models.FloatField()
#     reason = models.CharField(max_length=200)
#     credit_date = models.DateField()
#     is_deleted = models.BooleanField(default=False)