from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    posts = Artifact.objects.all()
    return render (request, 'stock/index.html', {'posts': posts, 'title': 'Главная страница', 'menu': menu})

def categories(request, cat_id):
    return HttpResponse(f'<h1>Товары по категориям</h1><p>{cat_id}</p>')

def archive(request, year):
    if int(year) < 2020:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def about(request):
    return render (request, 'stock/about.html', {'menu': menu, 'title': 'О нас'})