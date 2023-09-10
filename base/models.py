from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    thumbnail = models.ImageField(null=True, verbose_name='фото')
    body = RichTextUploadingField(verbose_name='описание')
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

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