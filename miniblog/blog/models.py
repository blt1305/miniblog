from django.db import models

class Post(models.Model):
    '''данные о посте в блоге'''
    title = models.CharField('Заголовок записи', max_length=255)
    anonse = models.CharField('Анонс записи', max_length=100, default='')
    description = models.TextField('Текст записи')
    photo = models.ImageField(upload_to='phpotos/%Y/%m/%d', blank=True)
    author = models.CharField('Автор записи', max_length=100)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_update = models.DateTimeField('Дата редактирования', auto_now=True)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


