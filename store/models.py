from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

