from rest_framework import serializers

from .models import Category, Product, Hotel, Item
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        ) 

class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            "id",
            "user_id",
            "name",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        ) 

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('city', 'state', 'email', 'name', 'last_name', 'account_address',  )

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "user_id",
            "name",
            "description",
            "price",
            "mse",
            "rmse",
            "minprice",
            "mindate",
            "get_plot",
            "get_image",
            "get_thumbnail"
        ) 