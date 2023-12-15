from rest_framework import serializers
from .models import Collection, CollectionMode, ShopModel
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

class CollectionModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionMode
        fields = '__all__'