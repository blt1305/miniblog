from django.db import models
from django.urls import reverse


class Category(models.Model):
    '''Класс для категории вещей, первичный по отношению к классу Artifact'''
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})



class Artifact(models.Model):
    '''класс для вещи на складе
    название, краткое описание, текст, фото, дата создания, дата изменения, опубликовано, автор'''
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.CharField(max_length=255)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})



