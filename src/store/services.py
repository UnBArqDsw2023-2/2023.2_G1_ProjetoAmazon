from abc import abstractmethod
from authuser.models import User
from store.models import *
from typing import Protocol

class CartService():
    def hasAccess(self, request):
        try:
            return User.objects.get(id=request.user.id)
        except:
            raise Exception('You must be logged in')

    def get_cart(self, user: User) -> Cart:
        cart, _ = Cart.objects.get_or_create(belongs_to=user)
        return cart

    def get_products_in_cart(self, cart: Cart):
        return CartProduct.objects.filter(cart=cart)

    def add_product_to_cart(self, cart: Cart, product: Product, quantity: int):
        cart_product, _ = CartProduct.objects.get_or_create(
            cart=cart,
            product__pk=product.pk,
            defaults={'product': product, 'quantity': 0}
        )

        cart_product.quantity += quantity
        cart_product.save()

    def getCart(self, request):
        try:
            user = self.hasAccess(request)
            cart = Cart.objects.get(belongs_to=user)
            return {'Cart':cart,'User':user}
        except Exception as e:
            raise Exception(e)

    def create_order_from_cart(self, user: User) -> Order:
        cart = Cart.objects.get(belongs_to=user)
        products_in_cart = cart.products.all()

        if len(products_in_cart) == 0:
            raise ValueError("Cart must contain products in order to make an order")

        order = Order.objects.create(made_by=user)
        order.products.set(products_in_cart)

        return order

class PaymentStrategy(Protocol):
    @abstractmethod
    def pay(self, payment_method: PaymentMethod) -> bool:
        raise NotImplementedError


class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, payment_method: PaymentMethod) -> bool:
        assert isinstance(payment_method, CreditCardPaymentMethod)

        # Interação com serviço externo de pagamento aqui.

        return True # ou False, caso o pagamento falhe

# Demais Strategies poderiam ser implementadas aqui.
# PixPaymentStrategy, TicketPaymentStrategy,
# GiftCardPaymentStrategy, BoletoPaymentStrategy

class PaymentStrategyFactory:
    _strategies: dict[PaymentMethod, PaymentStrategy]

    def __init__(self) -> None:
        self._strategies[CreditCardPaymentMethod] = CreditCardPaymentStrategy()
        # Inicialização das demais strategies aqui.

    def get_instance(self, payment_method: PaymentMethod) -> PaymentStrategy:
        strategy = self._strategies.get(payment_method)

        if strategy is None:
            raise ValueError(f"There is no payment strategy for {payment_method.__class__.__name__}")

        return strategy
