# 1 стандартный шаг создания моделей

from django.db import models
from django.urls import reverse

class Post(models.Model):
    article = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.article

# 2 не забываем про get_absolute_url

    def get_absolute_url(self):     #стандартное название, стоит выучить.
        return reverse('post', kwargs={'slug':  self.slug})
            #reverse ИМПОРТИРУЕМ,
            # post = указывает имя пути в urls.py
            #kwargs={'ключ':self.'значение'}
        #       создаем пару по slug:
                        # slug - указанаый в urls.py ...path('post/<slug:slug>/)...
                        # self.slug - указаное в поле модели Post ...slug = models.SlugField...
        #       создаем пару по id:
                        # post_id - указанаый в urls.py ...path('post/<int:post_id>/)...
                        # self.id - указаное в поле модели Post ...id = models....

# 3 создаем функцию для сохранения поля slug по оборазцу article. ЗАУЧИТЬ

    # def save(self, *args, **kwargs):
    #     self.###НАЗВАНИЕ ПОЛЯ СУРОГАТА### = slugify(self.###НАЗВАНИЕ ПОЛЕ ОБРАЗЦА###, allow_unicode=True)
    #     super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.article, allow_unicode=True)
        super().save(*args, **kwargs)

# 4 не забыть импортировать slugify
from django.utils.text import slugify
# Далее работа будет производиться только на латыне, любая форма заполненая кириллицей будет выдавать ошибку
# В админке в БД можно заметить что пост создается и SLUG поле заполняется, но браузер перестает читать ленту
# с постами имеющие поля slug на кириллице.

# 5
# что бы избежать проблему импортируем pytils.translit и добавляем в предыдущую функцию доп метод
# конвертации кириллицы в латынь

import pytils.translit

    def save(self, *args, **kwargs):
        self.slug = pytils.translit.translify(slugify(self.article, allow_unicode=True))
        super().save(*args, **kwargs)