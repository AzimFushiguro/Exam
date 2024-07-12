from django.db import models

class Company(models.Model):
    title = models.CharField("Name of company", max_length=255)
    product_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
class Product(models.Model):  # Changed 'Products' to 'Product' to follow Django's naming conventions

        price = models.IntegerField(default=0)
        title = models.CharField("Name of product", max_length=255)
        quantity = models.IntegerField(default=0)
        company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)  # Updated to reference the Company model correctly

        def __str__(self):
          return self.title


class Sales(models.Model):
     product = models.ForeignKey(Product.quantity, on_delete=models.CASCADE)
     quantity = models.IntegerField()
     sale_date = models.DateTimeField(auto_now_add=True)


     def str(self):
        return f"{self.quantity} units of {self.product.name} sold on {self.sale_date}"# class Product(models.Model):  # Changed 'Products' to 'Product' to follow Django's naming conventions
#     price = models.IntegerField(default=0)
#     title = models.CharField("Name of product", max_length=255)
#     quantity = models.IntegerField(default=0)
#     company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)  # Updated to reference the Company model correctly
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Product"
#         verbose_name_plural = "Products"
#
# class Sale(models.Model):
#     customer_name = models.CharField("Name of customer", max_length=255)
#     product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
#     product_quantity = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
#     sale_price = models.IntegerField(default=0)