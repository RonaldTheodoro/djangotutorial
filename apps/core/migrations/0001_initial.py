# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True, verbose_name='categoria')),
            ],
            options={
                'verbose_name_plural': 'categorias',
                'ordering': ['category'],
                'verbose_name': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor', models.CharField(max_length=50, unique=True, verbose_name='distribuidor')),
            ],
            options={
                'verbose_name_plural': 'distribuidores',
                'ordering': ['distributor'],
                'verbose_name': 'distribuidor',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=100, verbose_name='filme')),
                ('raised', models.DecimalField(decimal_places=3, max_digits=4, verbose_name='arrecadou')),
                ('liked', models.BooleanField(default=True, verbose_name='gostou')),
                ('realease', models.DateTimeField(verbose_name='lançamento')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_category', to='core.Category', verbose_name='categoria')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_distributor', to='core.Distributor', verbose_name='distribuidor')),
            ],
            options={
                'verbose_name_plural': 'filmes',
                'ordering': ['-realease'],
                'verbose_name': 'filme',
            },
        ),
    ]
