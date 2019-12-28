from django.db import models
from decimal import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.urls import reverse


class Customer(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    prime_customer = models.CharField(max_length=1, default='N', null=False)
    customer_since = models.DateField(auto_now = True, null=False)

    def __str__(self):
        return '{} \n {}'.format(self.first_name, self.last_name)

    class Meta:
         ordering = ('first_name',)


class Address(models.Model):

    fk = models.ForeignKey(Customer, default = 1, on_delete=models.CASCADE)
    street = models.CharField(max_length=25, null=False)
    city = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=25, null = False)
    zip = models.CharField(max_length=10, null = False)


    def __str__(self):
        return'Street: {} \nCity: {} \nState: {} \nZip: {}'.format(self.street, self.city, self.state, self.zip)
    class Meta:
         ordering = ('street',)

class Order(models.Model):
    payment_choice = (
        ('C','Credit'),
        ('A','Bank Account'),
        ('O', 'Other')
    )

    fk = models.ForeignKey(Customer, default = 1, on_delete=models.CASCADE)
    order_number = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now = True, null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=1, null=False, choices= payment_choice)
    exp_date = models.DateField(default=datetime.now()+timedelta(days=365), null=False)
    account_number = models.CharField(max_length=20, null=False)


    def __str__(self):
        return 'Name: {} \nOrder Number: {} \n Order Date: {} \ntotal: {}'.format(self.fk, self.order_number,self.order_date,self.total)
    class Meta:
        ordering = ('order_number',)


class Product(models.Model):
    fk = models.ForeignKey(Order, default =1, on_delete=models.CASCADE)
    description = models.CharField(max_length=25, null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return 'description: {} \n Quantity: {}'.format(self.description, self.quantity)
    class Meta:
        ordering = ('quantity',)

