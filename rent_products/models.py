from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300)
    product_reminder = models.TextField()
    price_per_month = models.FloatField()

    def __str__(self):
        return self.product_name
