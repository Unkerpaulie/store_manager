from django.db import models
from store.models import Store
from random import uniform


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=10)


class Subcategory(models.Model):
    subcategory_id = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=10)


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    # cost price will be randomly calculated to be between 3 and 8% lower than selling price
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.cost_price = round(self.selling_price * (1 - uniform(0.03, 0.08)), 2)
        super().save(*args, **kwargs)


class Stock(models.Model):
    stock_id = models.IntegerField(primary_key=True)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    stock_date = models.DateField(auto_now_add=True)
    discontinued_date = models.DateField(blank=True, null=True)
    