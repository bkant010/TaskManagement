# Generated by Django 2.2.8 on 2020-08-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='avatar',
            field=models.ImageField(upload_to=''),
        ),
    ]
