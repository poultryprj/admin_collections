from django.db import models
from django.contrib.auth.models import User
from routes.models import RouteModel

# Create your models here.


class ShopOwner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=100, null=True)
    owner_contactNo = models.CharField(max_length=15, null=True)
    owner_alternateNo = models.CharField(max_length=15, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shops_shop_owners')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.owner_name



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
        return self.shop_name
    


class ShopRoute(models.Model):
    shop_route_id  = models.AutoField(primary_key=True)
    route_id = models.ForeignKey(RouteModel, on_delete=models.SET_NULL, null=True)
    shop_id = models.ForeignKey(ShopModel, on_delete=models.SET_NULL, null=True)
    shop_order = models.CharField(max_length=10, null=True)




class ProductTypes(models.Model):
    product_type_id = models.AutoField(primary_key=True)
    product_type = models.CharField(max_length=100)

    def __str__(self):
        return self.product_type
    
    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"




class ProductCategories(models.Model):  
    product_category_id = models.AutoField(primary_key=True)
    product_category = models.CharField(max_length=100)

    def __str__(self):
        return self.product_category
    
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"



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


class Associations(models.Model):
    association_id = models.IntegerField(primary_key=True)
    association_name = models.CharField(max_length=500)
    association_sequence = models.IntegerField(null=True, default=None) 

    def __str__(self):
        return self.association_name   



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

   



