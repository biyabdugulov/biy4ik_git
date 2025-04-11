from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    year = models.DateField()
    product_type = models.BooleanField()
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.product_name
