from django.db import models

# Create your models here.

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        # return self.category_name + ' ' + self.categoryId
        return f"[Category ID: {self.categoryId}]  category name: {self.category_name} "


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "Product {} in category {}. Product ID: {}".format(self.product_name, self.category.category_name, self.productId )

    class Meta:
        ordering = ['category__category_name']    
