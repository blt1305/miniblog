from django import template
from stock.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter = None):
    '''вызов всех категорий'''
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk = filter)


@register.inclusion_tag('stock/list_categories.html')
def show_categories(sort = None, cat_selected = 0):
    '''создание html-страницы со всеми категориями'''
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}