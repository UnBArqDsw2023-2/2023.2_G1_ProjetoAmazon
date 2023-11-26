from django.shortcuts import render
from authuser.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def payment(request):
    return render(request, 'playment/payment.html')

def product(request):
    return render(request, 'products/product.html')

def cart(request):
    try:
        user = User.objects.get(id=request.user.id)
        return render(request, 'products/cart.html', {'user':user})
    except:
        messages.error(request, "You are not logged in")
        return render(request, 'index.html')
