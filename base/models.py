from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField


class Question(models.Model):
    TYPES = (
        ('backend', 'backend'),
        ('frontend', 'frontend'),
        ('fullstack', 'fullstack'),
        ('game', 'game'),
        ('app', 'app'),
    )
    answer = models.CharField(max_length=200, choices=TYPES, verbose_name='Вопрос')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    thumbnail = models.ImageField(null=True, verbose_name='фото')
    body = RichTextUploadingField(verbose_name='описание')
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Skill(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    body = models.TextField(null=True, blank=True, verbose_name='Содержание')
    logo = models.ImageField(null=True, blank=True, verbose_name='фото')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скилл'
        verbose_name_plural = 'Скиллы'


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Имя')
    body = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    created = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name} {self.body[0:50]}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Tag(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.CharField(max_length=200, verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Endorsement(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    body = models.TextField(verbose_name='Сообщение')
    approved = models.BooleanField(default=False,null=True, verbose_name='Отображение')
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-id']

    def __str__(self):
        return self.body[0:50]



