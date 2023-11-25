from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    NEWS = 'Новости'
    ARTICLE = 'Статья'
    PROGRAMMING = 'Программирование'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
        (PROGRAMMING, 'Программирование'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    categoryType = models.CharField(max_length=16, choices=CATEGORY_CHOICES, default=ARTICLE)
    title = models.CharField(max_length=200, verbose_name='заголовок')
    image = models.ImageField(null=True, verbose_name='фото')
    body = RichTextUploadingField(verbose_name='описание')
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    project = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    created = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name} {self.body[0:50]}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'