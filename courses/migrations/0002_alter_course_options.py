# Generated by Django 4.2.4 on 2023-10-12 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-id', '-created', 'title'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
    ]