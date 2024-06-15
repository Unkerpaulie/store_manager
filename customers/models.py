from django.db import models
from store.models import Store


class Region(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_name = models.CharField(max_length=10)

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)