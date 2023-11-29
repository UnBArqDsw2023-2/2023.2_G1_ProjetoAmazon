from django.shortcuts import render
from authuser.models import User
from django.contrib import messages
from store.models import Product
import json

from store.services import CartService

def index(request):
    #products = Product.objects.all()
    products = [{
        'name':"carrinho",
        'image':"{% static 'img/images.jpg'%}",
        'price':100.00,
        'description':"um carrinho controle remoto"
    }, {
        'name':"camisa do vasco",
        'image':"{% static 'img/images.jpg'%}",
        'price':100000,
        'description':"autografada pelo pec"
    },]
    return render(request, 'index.html',{'products':products})

def payment(request):
    return render(request, 'payment/payment.html',{'product':{
        'name':"carrinho",
        'image':"src\static\img\images.jpg",
        'price':100.00,
        'description':"um carrinho controle remoto",
        'sold_by':'caua',
        'amount_in_stock':10
    }})

def product(request):
    idProduct = request.GET.get('idProduct','')
    #selectedProduct = Product.objects.get(name=idProduct)

    #Basta adicionar selectedProduct em product,falta os dados no banco para testar 100%
    return render(request, 'products/product.html',{'product':{
        'name':"carrinho",
        'image':"src\static\img\images.jpg",
        'price':100.00,
        'description':"um carrinho controle remoto",
        'sold_by':'caua',
        'amount_in_stock':10
    }})

def cart(request):
    try:
        cartService = CartService()
        cart = cartService.getCart(request)
        if(request.method == 'POST'):
            idProduct = request.GET.get('idProduct','')
            selectedProduct = Product.objects.get(name=idProduct)
            cart.update(selectedProduct)
        return render(request, 'products/cart.html', {'cart':cart})
    except Exception as e:
        messages.error(request, e)
        #products = Product.objects.all()
        return render(request, 'index.html')
