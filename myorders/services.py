

# Python
from datetime import datetime

# Django
from django.db.models import Sum, DecimalField

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from .models import Customer, Order, Product, OrderItem




def calc_order_item_total_prices(order_item: OrderItem, product: Product, quantity: int):
    single_cost = product.cost
    total_cost = single_cost * total_cost

    


    
