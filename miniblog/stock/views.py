from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from django.views.generic import DetailView, UpdateView, DeleteView, View

from .models import *

menu = [
    {'title':'О сайте', 'url_name': 'about'},
    {'title':'Добавить статью', 'url_name':'add_page'},
    {'title':'Обратная связь', 'url_name':'contact'},
    {'title':'Войти','url_name':'login'}
]

def index(request):
    posts = Artifact.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats' : cats,
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0,}
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
    art = Artifact.objects.get(id=post_id)
    return render(request, 'stock/one_art.html', {'post': art})



def show_category(request, cat_id):
    posts = Artifact.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'title': 'Отображение по категориям',
        'menu': menu,
        'cat_selected': cat_id, }
    return render (request, 'stock/index.html', context=context)