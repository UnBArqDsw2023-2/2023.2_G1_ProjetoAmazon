from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from store.services import CartService
from store.models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

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

@login_required
def cart(request):
    cart_service = CartService()
    cart = cart_service.get_cart(request.user)
    products = cart_service.get_products_in_cart(cart)
    return render(request, 'products/cart.html', {'cart': cart, 'products': products})
