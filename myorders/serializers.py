# Rest-Framework
from dataclasses import fields
from rest_framework import serializers

# Project
from .models import Product, Customer, Order, OrderItem
from django.contrib.auth.models import User



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('created_at', 'modified_datetime')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'