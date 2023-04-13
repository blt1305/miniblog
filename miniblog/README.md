1. Структура: приложение blog отвечает за записи.

2. В первую очередь в blog создаем модель записи (ф-л miniblog/blog/models.py)
   class Post - задаем атрибуты (имена полей, тип данных)
   class Meta
![17-10-03.png](screens%2F17-10-03.png)

3. Регистрируем созданную модель в админке (miniblog/blog/admin.py)
    @admin.register, admin.ModelAdmin
    После изменения в моделях не забыть выполнить миграции!!!
![17-28-51.png](screens%2F17-28-51.png)