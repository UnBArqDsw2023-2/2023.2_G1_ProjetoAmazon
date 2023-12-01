from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from store.services import CartService, CartServiceProxy
from store.models import Product

cart_service = CartService()
cart_service_proxy = CartServiceProxy(cart_service)

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product.html', {'product': product})

class CartView(LoginRequiredMixin, View):
    cart_service = CartServiceProxy(CartService())

    def get(self, request):
        cart = self.cart_service.get_cart(request.user)
        products = self.cart_service.get_products(request.user)
        context = {'cart': cart, 'products': products}
        return render(request, 'products/cart.html', context)

    def post(self, request):
        product_id = int(request.POST['id'])
        amount = int(request.POST['amount'])

        product = Product.objects.get(pk=product_id)

        self.cart_service.add_product(request.user, product, amount)

        return redirect('cart')
