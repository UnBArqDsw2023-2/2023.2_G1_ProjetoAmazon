from django.shortcuts import render
from authuser.models import User
from django.contrib import messages
from store.models import Product

from store.services import CartService

def index(request):
    #products = Product.objects.all()
    products = [{
        'name':"carrinho",
        'img':"src\static\img\images.jpg",
        'preco':100.00,
        'descricao':"um carrinho controle remoto"
    }, {
        'name':"camisa do vasco",
        'img':"src\static\img\images.jpg",
        'preco':100000,
        'descricao':"autografada pelo pec"
    },]
    return render(request, 'index.html',{'products':products})

def payment(request):
    return render(request, 'playment/payment.html')

def product(request):
    product = Product.objects.get(name=request.GET.get('name'))
    return render(request, 'products/product.html',{'product':product})

def cart(request):
    try:
        cartService = CartService()
        user = cartService.getCart(request)
        return render(request, 'products/cart.html', {'user':user})
    except Exception as e:
        messages.error(request, e)
        return render(request, 'index.html')
