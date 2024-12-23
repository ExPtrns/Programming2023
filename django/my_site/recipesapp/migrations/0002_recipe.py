# Generated by Django 5.1.4 on 2024-12-21 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('steps', models.TextField()),
                ('cooking_time', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='recipes_photo/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipesapp.user')),
            ],
        ),
    ]