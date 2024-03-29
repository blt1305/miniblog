from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    '''Класс для категории вещей, первичный по отношению к классу Artifact'''
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']



class Artifact(models.Model):
    '''класс для вещи на складе
    название, краткое описание, текст, фото, дата создания, дата изменения, опубликовано, автор'''
    title = models.CharField(max_length=255, verbose_name='Название')
    summary = models.CharField(max_length=255, verbose_name='Описание')
    text = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.CharField(max_length=255, verbose_name='Автор')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'
        ordering = ['time_create', 'title']


class Comment(models.Model):
    user_email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Artifact, on_delete=models.CASCADE, verbose_name='Публикация')

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    '''лайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    post = models.ForeignKey(Artifact, verbose_name='Публикация', on_delete=models.CASCADE)