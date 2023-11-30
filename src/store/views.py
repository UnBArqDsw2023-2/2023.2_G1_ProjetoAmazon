from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from store.services import CartService
from store.models import CartProduct, Product

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

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product.html', {'product': product})

class CartView(LoginRequiredMixin, View):
    cart_service = CartService()

    def get(self, request):
        cart = self.cart_service.get_cart(request.user)
        products = self.cart_service.get_products_in_cart(cart)
        context = {'cart': cart, 'products': products}
        return render(request, 'products/cart.html', context)

    def post(self, request):
        product_id = int(request.POST['id'])
        amount = int(request.POST['amount'])

        product = Product.objects.get(pk=product_id)
        cart = self.cart_service.get_cart(request.user)

        cart_product, _ = CartProduct.objects.get_or_create(
            cart=cart,
            product__id=product_id,
            defaults={'product': product, 'quantity': 0},
        )

        cart_product.quantity += amount
        cart_product.save()

        return redirect('cart')
