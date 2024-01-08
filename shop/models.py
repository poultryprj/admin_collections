from django.db import models
from django.contrib.auth.models import User
from route.models import RouteModel
from vehicle.models import Vehicle

# Create your models here.


class ShopOwner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=100, null=True)
    owner_contactNo = models.CharField(max_length=15, null=True)
    owner_alternateNo = models.CharField(max_length=15, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shops_shop_owners')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ShopOwner_last_modified_by')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ShopOwner_deleted')


    def __str__(self):
        return self.owner_name
    
    class Meta:
        db_table = "ShopOwner"


class ShopModel(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_code = models.CharField(max_length=10, null=True)
    shop_name = models.CharField(max_length=100, null=True)
    shop_area = models.CharField(max_length=100, null=True)
    shop_latitude = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    shop_longitude = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    shop_address = models.CharField(max_length=100,null=True)
    shop_pincode = models.IntegerField(null=True)
    shop_distance = models.CharField(max_length=10, null=True)
    shop_mobileNo = models.CharField(max_length=15, null=True)
    shop_alternateNo = models.CharField(max_length=15, null=True)
    shop_ownerId = models.ForeignKey(ShopOwner, on_delete=models.SET_NULL, null=True)
    shop_type = models.CharField(max_length=20,null=True)
    shop_status = models.CharField(max_length=15,null=True)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.shop_name} ({self.shop_code}) "

    class Meta:
        db_table = "ShopModel"

class ShopRoute(models.Model):
    shop_route_id  = models.AutoField(primary_key=True)
    route_id = models.ForeignKey(RouteModel, on_delete=models.SET_NULL, null=True)
    shop_id = models.ForeignKey(ShopModel, on_delete=models.SET_NULL, null=True)
    shop_order = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "ShopRoute"


class ProductTypes(models.Model):
    product_type_id = models.AutoField(primary_key=True)
    product_type = models.CharField(max_length=100)

    def __str__(self):
        return self.product_type

    class Meta:
        db_table = "ProductTypes"


class ProductCategories(models.Model):  
    product_category_id = models.AutoField(primary_key=True)
    product_category = models.CharField(max_length=100)

    def __str__(self):
        return self.product_category
    
    class Meta:
        db_table = "ProductCategories"

class ProductMaster(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_typeId = models.ForeignKey(ProductTypes,on_delete=models.SET_NULL, null=True)
    product_value_on = models.CharField(max_length=100)   
    product_categoryId = models.ForeignKey(ProductCategories,on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='product_master_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='product_master_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='product_master_deleted')


    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "ProductMaster"

class Associations(models.Model):
    association_id = models.IntegerField(primary_key=True)
    association_name = models.CharField(max_length=500)
    association_sequence = models.IntegerField(null=True, default=None) 

    def __str__(self):
        return self.association_name   
    
    class Meta:
        db_table = "Associations"



class ShopProductRates(models.Model):
    shop_product_rates_id = models.AutoField(primary_key=True)
    shopId	= models.ForeignKey(ShopModel, on_delete=models.SET_NULL, null=True)
    associationId = models.ForeignKey(Associations, on_delete=models.SET_NULL, null=True)    
    ProductId	= 	models.ForeignKey(ProductMaster, on_delete=models.SET_NULL, null=True)      
    rate_margin = models.IntegerField()
    flexible_yn = models.CharField(max_length=15,null=True)
    flexible_formula = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop_product_rates_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop_product_rates_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop_product_rates_deleted')

    class Meta:
        db_table = "ShopProductRates"
    

class ShopBalance(models.Model):
    shop_balance_id = models.AutoField(primary_key=True)
    shopId = models.ForeignKey(ShopModel, on_delete=models.SET_NULL, null=True)
    balance_date = models.DateField()
    balance = models.FloatField()
    active = models.CharField(max_length=15,null=True, default='Yes')
    adjustment_amount = models.FloatField(null=True)
    adjustment_remark = models.TextField(null=True)
    balance_utc_date = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop_balance_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop_balance_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop_balance_deleted')

    class Meta:
        db_table = "ShopBalance"


class ShopFlexibleRate(models.Model):
    shop_flexible_rate_id = models.AutoField(primary_key=True)
    flexible_rate_date = models.DateField()
    shopId = models.ForeignKey(ShopModel, on_delete=models.SET_NULL, null=True)
    product_typeId = models.ForeignKey(ProductTypes, on_delete=models.SET_NULL, null=True)
    flexible_rate = models.FloatField()
    flexible_formula = models.IntegerField(null=True)
    sell_rate = models.FloatField()
    with_skin = models.FloatField()
    without_skin = models.FloatField()
    sms_send_yn = models.CharField(max_length=15,null=True, default='No')
    sms_replyId = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop_flexible_rate_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop_flexible_rate_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop_flexible_rate_deleted')

    class Meta:
        db_table = "ShopFlexibleRate"

class ProductRecieve(models.Model):
    product_record_id = models.AutoField(primary_key=True)
    recieved_date = models.DateField(null=True)
    vendorId = models.ForeignKey('vendor.Vendor',on_delete=models.SET_NULL, null=True)
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
    driverId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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
    delete_reason = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.product_record_id)

    class Meta:
        db_table = "ProductRecieve"

class ProductIssue(models.Model):
    product_issue_id = models.AutoField(primary_key=True)
    issue_date = models.DateField(null=True)
    shopId = models.ForeignKey(ShopModel, on_delete=models.SET_NULL, null=True)
    paper_rate = models.FloatField()
    boiler_size = models.CharField(max_length=20)
    issue_birds = models.CharField(max_length=20)
    birds_weight = models.FloatField()
    daily_rate = models.FloatField()
    issue_amount = models.FloatField()
    vehicleId = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    driverId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    entry_source = models.IntegerField()
    latitude = models.DecimalField(max_digits=20, decimal_places=5,null=True)
    longtitude = models.DecimalField(max_digits=20, decimal_places=5,null=True)
    product_typeId = models.ForeignKey(ProductTypes,on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ProductIssue_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ProductIssue_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ProductIssue_deleted')

    class Meta:
        db_table = "ProductIssue"

class ShopProductRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    shopId = models.ForeignKey(ShopModel, on_delete=models.SET_NULL, null=True)
    product_request_date_time = models.DateTimeField(null=True)
    productId = models.ForeignKey(ProductMaster,on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=20, decimal_places=2,null=True)
    status = models.CharField(max_length=100,default="Rejected") #Status Approved / Rejected
    delivery_date_time = models.DateTimeField(null=True)
    driverId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ShopProductRequest_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ShopProductRequest_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ShopProductRequest_deleted')
    
    def __str__(self):
        return str(self.request_id)

    class Meta:
        db_table = "ShopProductRequest"
