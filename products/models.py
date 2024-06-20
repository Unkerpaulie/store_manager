from django.db import models
from store.models import Store


class Category(models.Model):
    category_name = models.CharField(max_length=10)
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "subcategories"

    def __str__(self):
        return self.subcategory_name


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name


class Stock(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    stock_date = models.DateField(auto_now_add=True)
    discontinued_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} of {self.product} on {self.stock_date}"

    