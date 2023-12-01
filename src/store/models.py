from django.db import models
from authuser.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    sold_by = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    price = models.FloatField()
    amount_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    belongs_to = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    products = models.ManyToManyField(Product, through='CartProduct')

    def total_price(self) -> float:
        return sum(
            x.product.price * x.quantity
            for x in CartProduct.objects.filter(cart=self)
        )

    def __str__(self):
        return f'Cart ({self.belongs_to.email})'


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.product.name} ({self.quantity}) {self.cart.belongs_to.email}'

class PaymentMethod(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class CreditCardPaymentMethod(PaymentMethod):
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiration_date = models.CharField(max_length=10)


class Order(models.Model):
    date = models.DateField(default=timezone.now)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE,
        null=True,
    )

    products = models.ManyToManyField(Product, through='OrderProduct')
    discount_percentage = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99.99),
        ]
    )

    def final_value(self) -> float:
        value = sum(
            x.product.price * x.quantity
            for x in OrderProduct.objects.filter(order=self)
        )
        return value * (1 - (self.discount_percentage / 100))

    def __str__(self) -> str:
        return f'Order ({self.made_by.name})'

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

