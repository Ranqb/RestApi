# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pizzashopapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashopapp', '0004_auto_20171210_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to=pizzashopapp.models.news_upload_path)),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.PizzaShop')),
            ],
        ),
    ]