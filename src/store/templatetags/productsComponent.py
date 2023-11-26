from django import template

register = template.Library()

@register.inclusion_tag('components/productCard.html')
def showProductCard(product = 1):
    product = {
        'name':"carrinho",
        'img':"src\static\img\images.jpg",
        'preco':100.00,
        'descricao':"um carrinho controle remoto"
    }
    return {'product': product}