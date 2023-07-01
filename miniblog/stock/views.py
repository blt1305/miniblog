from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title':'О сайте', 'url_name': 'about'},
    {'title':'Добавить статью', 'url_name':'add_page'},
    {'title':'Обратная связь', 'url_name':'contact'},
    {'title':'Войти','url_name':'login'}
]

def index(request):
    posts = Artifact.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'menu': menu}
    return render (request, 'stock/index.html', context=context)


def about(request):
    return render (request, 'stock/about.html', {'menu': menu, 'title': 'О сайте'})



def add_page(request):
    return render (request, 'stock/add_page.html', {'menu': menu, 'title': 'Добавить статью'})


def contact(request):
    return render (request, 'stock/contact.html', {'menu': menu, 'title': 'Обратная связь'})

def login(request):
    return render(request, 'stock/login.html', {'menu': menu, 'title': 'Войти'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')