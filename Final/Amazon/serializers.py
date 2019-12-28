from rest_framework import serializers
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from .models import *
from .serializers import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','first_name', 'last_name', 'prime_customer', 'customer_since')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'fk', 'street', 'city','state','zip')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ( 'order_number', 'fk', 'order_date','total','payment_type','exp_date','account_number')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'fk', 'description', 'quantity',)
