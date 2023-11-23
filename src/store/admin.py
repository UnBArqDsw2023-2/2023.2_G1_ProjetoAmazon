from django.contrib import admin

from store.models import Store, Product

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount_in_stock', 'sold_by']
