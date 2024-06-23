from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Store(models.Model):
    store_name = models.CharField(max_length=100, default="My Store")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    daily_customers = models.IntegerField(default=20)
    start_balance = models.IntegerField(default=100000)
    open_date = models.DateField(default=date(date.today().year - 10, 1, 1))

    def __str__(self):
        return self.store_name

