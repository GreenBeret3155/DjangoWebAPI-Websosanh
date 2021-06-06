from rest_framework import serializers 
from .models import *

class ProductKeyDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
        )

class KeySerializers(serializers.ModelSerializer):
    link_img = serializers.CharField(allow_null=True)
    products = ProductKeyDisplaySerializer(many = True, read_only = True)
    min_price = serializers.CharField(allow_null=True)

    class Meta:
        model = Key
        fields = (
            'id', 
            'name',
            'link_img',
            'transformed_name', 
            'brand',  
            'Ram', 
            'Bonhotrong', 
            'Pin', 
            'products', 
            'min_price'           
        )

class NoiBanSerrializers(serializers.ModelSerializer):

    class Meta:
        model = Noi_ban
        fields = (
            'id',
            'name',
        )

class ProductSerializer(serializers.ModelSerializer):
    noi_ban = serializers.ReadOnlyField(source='noi_ban.name')  

    class Meta:
        model = Product
        fields = (
            'id', 
            'name',
            'link', 
            'link_img', 
            'price_sale', 
            'price_goc', 
            'brand', 
            'manhinh', 
            'hedieuhanh', 
            'cameratruoc', 
            'CPU', 
            'Ram', 
            'Bonhotrong', 
            'Pin',
            'noi_ban'
        )