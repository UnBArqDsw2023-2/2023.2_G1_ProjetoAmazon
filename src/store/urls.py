from django.urls import path

from store.views import *

urlpatterns = [
    path('', index, name="index"),
    path('product/<int:id>', product, name="product"),
    path('payment/', payment, name="payment"),
    path('cart/', CartView.as_view() , name="cart")
]
