# Generated by Django 2.2.8 on 2020-08-07 04:25

from django.db import migrations, models
import taskapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_auto_20200807_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='avatar',
            field=models.ImageField(upload_to=taskapp.models.project_image_store),
        ),
    ]