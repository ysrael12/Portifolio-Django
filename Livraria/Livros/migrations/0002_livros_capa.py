# Generated by Django 4.1.2 on 2022-10-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='capa',
            field=models.ImageField(default=None, upload_to='profile_images'),
        ),
    ]
