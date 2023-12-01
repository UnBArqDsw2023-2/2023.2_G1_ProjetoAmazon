from abc import abstractmethod
from authuser.models import User
from store.models import *
from typing import Protocol

from django.core.exceptions import ObjectDoesNotExist

class CartServiceProtocol(Protocol):
    @abstractmethod
    def get_cart(self, user: User) -> Cart:
        raise NotImplementedError

    @abstractmethod
    def add_product(self, user: User, product: Product, quantity: int):
        raise NotImplementedError

    @abstractmethod
    def get_products(self, user: User) -> list[CartProduct]:
        raise NotImplementedError

    @abstractmethod
    def create_order(self, user: User) -> Order:
        raise NotImplementedError

class CartService(CartServiceProtocol):
    def get_cart(self, user: User) -> Cart:
        cart, _ = Cart.objects.get_or_create(belongs_to=user)
        return cart

    def add_product(self, user: User, product: Product, quantity: int):
        cart = self.get_cart(user)

        cart_product, _ = CartProduct.objects.get_or_create(
            cart=cart,
            product__pk=product.pk,
            defaults={'product': product, 'quantity': 0}
        )

        cart_product.quantity += quantity
        cart_product.save()

    def get_products(self, user: User) -> list[CartProduct]:
        cart = self.get_cart(user)
        return list(CartProduct.objects.filter(cart=cart))

    def create_order(self, user: User) -> Order:
        cart = self.get_cart(user)
        products_in_cart = cart.products.all()

        if len(products_in_cart) == 0:
            raise ValueError("Cart must contain products in order to make an order")

        order = Order.objects.create(made_by=user)
        order.products.set(products_in_cart)

        return order


class CartServiceProxy(CartServiceProtocol):
    _service: CartService

    def __init__(self, service: CartService) -> None:
        self._service = service

    def get_cart(self, user: User) -> Cart:
        self._check_access(user)
        return self._service.get_cart(user)

    def add_product(self, user: User, product: Product, quantity: int):
        self._check_access(user)
        return self._service.add_product(user, product, quantity)

    def get_products(self, user: User) -> list[CartProduct]:
        self._check_access(user)
        return self._service.get_products(user)

    def create_order(self, user: User) -> Order:
        self._check_access(user)
        return self._service.create_order(user)

    def _check_access(self, user: User):
        try:
            User.objects.get(pk=user.pk)
        except ObjectDoesNotExist:
            raise ValueError("You must be authenticated")

# No python não existem Interfaces, e sim Protocolos. Funcionalmente, elas são
# iguais. No entanto, como o Python é uma linguagem dinamicamente tipada, não
# existe check em tempo de compilação para garantir que o protocolo está implementado
# corretamente. Ferramentas como MyPy podem ser usadas para obter essa garantia.
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
    _strategies: dict[str, PaymentStrategy]

    def __init__(self) -> None:
        self._strategies[CreditCardPaymentMethod.__class__.__name__] = CreditCardPaymentStrategy()
        # Inicialização das demais strategies aqui.

    def get_instance(self, payment_method: PaymentMethod) -> PaymentStrategy:
        strategy = self._strategies.get(payment_method.__class__.__name__)

        if strategy is None:
            raise ValueError(f"There is no payment strategy for {payment_method.__class__.__name__}")

        return strategy
