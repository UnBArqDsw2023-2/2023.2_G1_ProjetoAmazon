from django.contrib import admin

from store.models import *

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount_in_stock', 'sold_by','image']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(CreditCardPaymentMethod)
class CreditCardPaymentMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'made_by', 'final_value']


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass
