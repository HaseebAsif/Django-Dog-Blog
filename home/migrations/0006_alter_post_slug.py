# Generated by Django 3.2.3 on 2022-02-03 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]