from rest_framework import serializers
from django.contrib.auth.models import Group
from route.models import RouteModel
from shop.models import ProductRecieve, ProductIssue, ShopModel, ShopProductRequest
from vehicle.models import Vehicle, VehicleRunning
from .models import Collection, CollectionMode, Complaint, SkipShop
from django.contrib.auth.models import User


class ShopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields = '__all__'



class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'



class RouteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        
class CollectionModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionMode
        fields = '__all__'



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'



class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class ProductRecieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRecieve
        fields = '__all__'



class ProductIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIssue
        fields = '__all__'

class SkipShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkipShop
        fields = '__all__'



class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'

class VehicleRunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleRunning
        fields = '__all__'

class ShopProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProductRequest
        fields = '__all__'  # Include all fields from the model
