from django.db import models


class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phone = models.IntegerField()


class Order(models.Model):
    product = models.CharField(max_length=40)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
