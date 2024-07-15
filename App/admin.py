from django.contrib import admin
from App.models import Product, Company, Sales
from django.contrib.auth.models import Group, User

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "quantity", "company")

    def has_change_permission(self, request, obj=None):
        if obj and obj.company == True:
            return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.quantity == 0:
            return False
        return True


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "product_count")

    def has_delete_permission(self, request, obj=None):
        if obj and obj.product_count != 0:
            return False
        return True


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ("id", "costumer_name", "product", "product_count", "sale_cost")

    def has_change_permission(self, request, obj=None):
        return False
