# Generated by Django 4.2.4 on 2023-09-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
