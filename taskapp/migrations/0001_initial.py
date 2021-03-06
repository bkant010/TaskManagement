# Generated by Django 2.2.8 on 2020-08-07 04:04

from django.db import migrations, models
import django.db.models.deletion
import taskapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('avatar', models.ImageField(upload_to=taskapp.models.project_image_store)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('projects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taskapp.Projects')),
            ],
        ),
    ]
