Изменения по отношению к базовому проекту selfedu
______________________
Использовала другой вариант подключения статических файлов.
Я - подключила бутстрап, 
![19-44-50.png](screens%2F19-44-50.png)

связь с базовым шаблоном у меня прописана так:
link rel="stylesheet" href="{% static 'stock/css/styles.css' %}">
![19-48-16.png](screens%2F19-48-16.png)

Картинка на сайте в итоге такая:
![19-48-36.png](screens%2F19-48-36.png)

В лекции selfedu изначально было так:
link type="text/css" href="{% static 'stock/css/styles.css' %}" rel="stylesheet" />
![19-42-41.png](screens%2F19-42-41.png)
______________________________