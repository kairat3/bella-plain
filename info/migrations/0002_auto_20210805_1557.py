# Generated by Django 3.2.5 on 2021-08-05 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
    ]
