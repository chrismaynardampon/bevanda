from django.db import models


class Inventory(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    stock = models.IntegerField()
    quantity = models.IntegerField()
    event_date = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name

class PreparationInventory(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    transfer_date = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    ingredient_type = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    stock_in_date = models.DateField(null=True, blank=True)
    stock_out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.product_name
    
class EventBooking(models.Model):
    event_date = models.DateField()
    event_time = models.TimeField()

    def __str__(self):
        return f"Booking on {self.event_date} at {self.event_time}"