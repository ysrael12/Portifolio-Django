# Generated by Django 4.1.2 on 2022-10-18 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Livros', '0006_alter_livros_capa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='capa',
        ),
    ]
