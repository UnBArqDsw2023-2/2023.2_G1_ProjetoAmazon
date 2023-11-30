from authuser.models import User
from store.models import Cart, Order, CartProduct

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

    def getCart(self, request):
        try:
            user = self.hasAccess(request)
            cart = Cart.objects.get(belongs_to=user)
            return {'Cart':cart,'User':user}
        except Exception as e:
            raise Exception(e)

    def create_order_from_cart(self, user: User) -> Order:
        breakpoint()

        cart = Cart.objects.get(belongs_to=user)
        products_in_cart = cart.products.all()

        if len(products_in_cart) == 0:
            raise ValueError("Cart must contain products in order to make an order")

        order = Order.objects.create(made_by=user)
        order.products.set(products_in_cart)

        return order
