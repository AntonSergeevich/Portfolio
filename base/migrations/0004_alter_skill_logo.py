# Generated by Django 4.2.4 on 2023-10-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='фото'),
        ),
    ]