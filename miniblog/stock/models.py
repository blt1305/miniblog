from django.db import models

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

    def __str__(self):
        return self.title