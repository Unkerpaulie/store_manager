from django.db import models
from store.models import Store


class Region(models.Model):
    region_name = models.CharField(max_length=10)

    def __str__(self):
        return self.region_name
    

class Customer(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    