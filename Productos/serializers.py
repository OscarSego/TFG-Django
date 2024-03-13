from rest_framework import serializers
from .models import Producto, UserItemCarrito, UserCarrito


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserItemCarrito
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(many=True, read_only=True)

    class Meta:
        model = UserCarrito
        fields = '__all__'