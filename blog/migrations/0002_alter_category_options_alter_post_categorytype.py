# Generated by Django 4.2.4 on 2023-11-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('Новости', 'Новость'), ('Статья', 'Статья'), ('Программирование', 'Программирование')], default='Статья', max_length=16),
        ),
    ]
