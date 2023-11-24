from django.db import models
from django.utils import timezone
from abc import ABC, abstractmethod
from authuser.models import User

class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    sold_by = models.ForeignKey(Store, on_delete=models.CASCADE)

    price = models.FloatField()
    amount_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CartProxy(ABC):
    @abstractmethod
    def addProduct(self, product:Product):
        pass

    @abstractmethod
    def removeProduct(self, product:Product):
        pass

    @abstractmethod
    def listProducts(self):
        pass

    @abstractmethod
    def getPrice(self):
        pass

class Cart(type(models.Model),type(CartProxy)):
    price = models.FloatField()
    products: Product = []

    def addProduct(self, product:Product):
        if product not in self.products:
            self.products.append(product)
            self.price += product.price

    def removeProduct(self, product:Product):
        self.products.remove(product)

    def listProducts(self):
        return self.products

    def getPrice(self):
        return self.price


class CartService(type(models.Model),type(CartProxy)):

    realCart:Cart

    def __init__(self,realCart:Cart):
        self.realCart = realCart

    def checkLogin(self):
        return 1

    def addProduct(self, product:Product):
        if(self.checkLogin()):
            self.realCart.addProduct(product)

    def removeProduct(self, product:Product):
        if(self.checkLogin()):
            self.realCart.removeProduct(product)

    def listProducts(self):
        if(self.checkLogin()):
            return self.realCart.listProducts()

    def getPrice(self):
        if(self.checkLogin()):
            return self.realCart.getPrice()

class Order(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    orderDate = models.DateField()
    status = models.CharField(max_length=250)
    cart:CartService
    account: User
    value = models.FloatField()

    def __init__(self):
        pass

    def describeOrder(self):
        pass

    def generatePayment(self):
        payment = Payment()


class PaymentMode(ABC):
    @abstractmethod
    def pay(self,data):
        pass

    @abstractmethod
    def generate(self,data):
        pass

class Payment(models.Model):
    paymentId = models.UUIDField(primary_key=True,editable=False)
    value = models.FloatField()
    actualData = models.DateField(default=timezone.now())
    expirationData = models.DateField()
    status = models.TextField(blank=True,default="")
    costOfFreight = models.FloatField()
    coupon = models.BooleanField()
    discount = models.FloatField()
    finalValue = models.FloatField()
    paymentMode:PaymentMode = models.Model

    def __init__(self,costOfFreight,coupon,discount,value):
        self.costOfFreight = costOfFreight
        self.coupon = coupon
        self.discount = discount
        self.value = value

    def __str__(self):
        return self.paymentId

    def setPaymentMode(self,paymentMode):
        self.paymentMode = paymentMode

    def payValue(self):
        self.paymentMode.pay()

    def generatePayment(self):
        self.paymentMode.generate()

    def verifyStatus(self):
        return self.status

    def sumCostOfFreight(self):
        return self.costOfFreight

    def finish(self):
        pass

class Pix(type(models.Model),type(PaymentMode)):
    chavePix = models.CharField(max_length=250)

    def pay(self,data):
        pass

    def generate(self,data):
        pass

class Ticket(type(models.Model),type(PaymentMode)):
    barCode = models.CharField(max_length=250)
    recipientName = models.CharField(max_length=250)
    recipientCPF = models.CharField(max_length=14)

    def __init__(self,recipientName,recipientCPF):
        self.recipientCPF = recipientCPF
        self.recipientName = recipientName

    def pay(self,data):
        pass

    def generate(self,data):
        pass

class CreditCard(type(models.Model),type(PaymentMode)):
    cardName = models.CharField(max_length=250)
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expirationDate = models.CharField(max_length=10)

    def pay(self,data):
        pass

    def generate(self,data):
        pass
