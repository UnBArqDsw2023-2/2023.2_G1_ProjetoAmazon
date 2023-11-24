from django.urls import path

from store.views import *

urlpatterns = [
    path('', index,name="index"),
    path('product/',product,name="product"),
    path('payment/',payment,name="payment")
]
