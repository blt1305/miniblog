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

@register.simple_tag()
def get_menu():
    '''возвращает контекстное меню'''
    menu = [
        {'title': 'Главная', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
    ]
    return menu

@register.inclusion_tag('stock/list_menu.html')
def show_menu():
    '''создание html-фрагмента с контекстным меню'''
    menu = [
        {'title': 'Главная', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
    ]
    return {'menu': menu}