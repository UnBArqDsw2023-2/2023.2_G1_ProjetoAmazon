from django import template

register = template.Library()

@register.inclusion_tag('components/productCard.html')
def showProductCard(product):
    return {'product': product}