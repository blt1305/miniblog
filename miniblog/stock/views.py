from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse ('Страница приложения stock.')

def categories(request, catid):
    return HttpResponse(f'<h1>Товары по категориям</h1><p>{catid}</p>')

def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')