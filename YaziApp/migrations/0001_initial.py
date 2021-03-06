# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoriler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(help_text='Kategoriye vereceğiniz başlığı giriniz.', max_length=40, verbose_name='Kategori adı')),
                ('sef', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Kategoriler',
            },
        ),
    ]
