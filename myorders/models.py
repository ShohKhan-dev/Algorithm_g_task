
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    name  = models.CharField(max_length=50)
    tel_number = models.CharField(max_length=50)
    dept = models.IntegerField()

    def __str__(self):
        return self.name

    

class Order(models.Model):

    NEW = 'new'
    WAITING = 'waiting'
    PROCESSES = 'processes'
    DONE = 'done'
    REJECT = 'reject'

    STATUS = (
        (NEW, NEW),
        (WAITING, WAITING),
        (PROCESSES, PROCESSES),
        (DONE, DONE),
        (REJECT, REJECT)
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='made_orders')
    created_at = models.DateTimeField(auto_now_add=True)
    summa = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default=NEW)

    modified_datetime = models.DateTimeField(auto_now=True)


    def return_new_update(self):
        self.status = 'new'
        self.save()
    


class Product(models.Model):
    name  = models.CharField(max_length=255)
    cost = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name




class OrderItem(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_products')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return self.product.name




