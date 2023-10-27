from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Order(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(max_length=100, null=True, blank=True)
    complete = models.BooleanField(default=False, null = True, blank=True)
    order_num = models.IntegerField(default=0, null=0, blank=True)

    def __str__(self):
        return str(self.order_num)
    
    @property
    def get_order_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.CharField(max_length=200, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=0, blank=True)
    price = models.IntegerField(default=0, null=0, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.price * self.quantity
        return total

class ShippingAddress(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address