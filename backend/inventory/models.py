from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)

class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    api_endpoint = models.URLField()
    api_key = models.CharField(max_length=100)

class ReorderRequest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, default='Pending')
    requested_at = models.DateTimeField(auto_now_add=True)
