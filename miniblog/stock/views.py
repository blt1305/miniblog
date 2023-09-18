from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from django.views.generic import DetailView, UpdateView, DeleteView, View
from .models import *
from .forms import *



def index(request):
    posts = Artifact.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,}
    return render (request, 'stock/index.html', context=context)


def about(request):
    return render (request, 'stock/about.html', { 'title': 'О сайте'})


def add_page(request):
    if request.method == 'POST':
        form = AddStockForm(request.POST)
        if form.is_valid():
            try:
                Artifact.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None,'Oшибка при добавлении записи')
    else:
        form = AddStockForm()
    return render (request, 'stock/add_page.html', {'form': form, 'title': 'Добавить статью'})


def contact(request):
    return render (request, 'stock/contact.html', { 'title': 'Обратная связь'})

def login(request):
    return render(request, 'stock/login.html', { 'title': 'Войти'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    art = Artifact.objects.get(id=post_id)
    context = {
        'post': art,
        'title': art,
    }
    return render(request, 'stock/one_art.html', context=context)



def show_category(request, cat_id):
    posts = Artifact.objects.filter(cat_id=cat_id)

    context = {
        'posts': posts,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id, }
    return render (request, 'stock/index.html', context=context)

class AddComment(View):
    def post(self, request, post_id):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.post_id = post_id
                form.save()
        return redirect(f'/{post_id}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, post_id):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip = ip_client, post_id = post_id)
            return redirect(f'/{post_id}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(post_id)
            new_like.save()
            return redirect(f'/{post_id}')


class DelLike(View):
    def get(self, request, post_id):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip = ip_client)
            lik.delete()
            return redirect(f'/{post_id}')
        except:
            return redirect(f'/{post_id}')