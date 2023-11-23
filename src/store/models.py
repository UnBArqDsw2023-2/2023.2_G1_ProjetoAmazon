from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    sold_by = models.ForeignKey(Store, on_delete=models.CASCADE)

    price = models.FloatField()
    amount_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
