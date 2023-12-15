from rest_framework import serializers

from routes.models import RouteModel
from .models import Collection, ShopModel, UserModel


class ShopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields = '__all__'



class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'



class RouteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        fields = '__all__'