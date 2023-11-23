from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def payment(request):
    return render(request, 'payment.html')

def product(request):
    return render(request, 'product.html')