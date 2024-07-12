from django.contrib import admin
from App.models import Product,Company,Sale
from django.contrib.auth.models import Group, User

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Sale)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "quantity","company")
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id","title","product_count")