from django.shortcuts import render
from authuser.models import User
from django.contrib import messages

from store.services import CartService

def index(request):
    return render(request, 'index.html')

def payment(request):
    return render(request, 'playment/payment.html')

def product(request):
    return render(request, 'products/product.html')

def cart(request):
    try:
        cartService = CartService()
        user = cartService.getCart(request)
        return render(request, 'products/cart.html', {'user':user})
    except Exception as e:
        messages.error(request, e)
        return render(request, 'index.html')
