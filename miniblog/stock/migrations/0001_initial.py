# Generated by Django 4.2.3 on 2023-09-18 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('summary', models.CharField(max_length=255, verbose_name='Описание')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Вещь',
                'verbose_name_plural': 'Вещи',
                'ordering': ['time_create', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IP-адрес')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.artifact', verbose_name='Публикация')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text_comments', models.TextField(max_length=2000, verbose_name='Текст комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.artifact', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AddField(
            model_name='artifact',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.category', verbose_name='Категория'),
        ),
    ]
