from django.db import models
from authuser.models import User
from django.utils import timezone

class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    sold_by = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField()

    price = models.FloatField()
    amount_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Cart ({self.belongs_to.name})'

class Order(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    orderDate = models.DateField()
    status = models.CharField(max_length=250)
    cart: models.ForeignKey(Cart, on_delete=models.CASCADE)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField()

    def describeOrder(self):
        pass
    def generatePayment(self):
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

    def __str__(self):
        return self.paymentId

    def verifyStatus(self):
        return self.status

    def sumCostOfFreight(self):
        return self.costOfFreight

    def finish(self):
        pass

class Pix(Payment):
    chavePix = models.CharField(max_length=250)
    def pay(self,data):
        pass

    def generate(self,data):
        pass

class Ticket(Payment):
    barCode = models.CharField(max_length=250)
    recipientName = models.CharField(max_length=250)
    recipientCPF = models.CharField(max_length=14)

    def pay(self,data):
        pass
    def generate(self,data):
        pass

class CreditCard(Payment):
    cardName = models.CharField(max_length=250)
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expirationDate = models.CharField(max_length=10)

    def pay(self,data):
        pass
    def generate(self,data):
        pass
