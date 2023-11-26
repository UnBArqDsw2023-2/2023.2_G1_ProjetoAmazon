from authuser.models import User
from store.models import Cart

class CartService():
    def hasAccess(self, request):
        try:
            return User.objects.get(id=request.user.id)
        except:
            raise Exception('You must be logged in')

    def getCart(self,request):
        try:
            user = self.hasAccess(request)
            cart = Cart.objects.get(belongs_to=user)
            return {'Cart':cart,'User':user}
        except Exception as e:
            raise Exception(e)
