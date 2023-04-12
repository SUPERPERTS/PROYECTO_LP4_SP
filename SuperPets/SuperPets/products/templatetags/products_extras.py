from django import template
from products.models import Product

register = template.Library()

@register.simple_tag
def get_product_list():
    products = Product.objects.all()
    return products