from django.db import models

class Post(models.Model):
    '''данные о посте в блоге'''
    title = models.CharField('Заголовок записи', max_length=50)
    #anonse = models.CharField('Анонс записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Автор записи', max_length=100)
    date = models.DateField('Дата')


    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


