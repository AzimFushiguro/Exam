from django.core.exceptions import ValidationError
from django.db import models


class Company(models.Model):
    title = models.CharField("Kompanyaning nomi", max_length=255)
    product_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Product(models.Model):  # Changed 'Products' to 'Product' to follow Django's naming conventions
    price = models.IntegerField(default=0)
    title = models.CharField("Maxsulot nomi", max_length=255)
    quantity = models.IntegerField(default=0)
    company = models.ForeignKey(Company, null=True, blank=True,
                                on_delete=models.CASCADE)  # Updated to reference the Company model correctly

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Sales(models.Model):
    costumer_name = models.CharField("Mijoz nomi", max_length=255)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    product_count = models.IntegerField("Masxulot soni")
    sale_cost = models.IntegerField()
    # sale_date = models.DateTimeField("Sotilgan Sana", auto_now_add=True)

    def __str__(self):
        return self.costumer_name

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def clean(self):
        if self.product and self.product_count > self.product.quantity:
            raise ValidationError("Some products do not have sufficient quantity.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Perform validation before saving

        if self.product:
            self.product.quantity -= self.product_count
            self.product.save()

        super().save(*args, **kwargs)
