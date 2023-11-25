from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Category(models.Model):
    img = models.ImageField(blank=True)
    name = models.CharField(max_length=10, db_index=True, verbose_name='Какой курс')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Course(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Курс', null=True)
    title = models.CharField(max_length=250, verbose_name='Тема')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    desc = RichTextUploadingField(verbose_name='Описание')
    img = models.ImageField(blank=True)
    created = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Дата')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['id']
