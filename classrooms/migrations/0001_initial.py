# Generated by Django 3.1.3 on 2020-11-11 19:53

import classrooms.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '0. Rooms',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='classrooms.room')),
                ('route', models.CharField(default='meet', editable=False, max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('breakout_rooms', classrooms.models.IntegerRangeField()),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '1. Class Rooms',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('classes', models.ManyToManyField(blank=True, to='classrooms.Classroom')),
            ],
            options={
                'verbose_name_plural': '2. Teachers',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('iframe', models.URLField()),
                ('logo', models.URLField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('classes', models.ManyToManyField(blank=True, to='classrooms.Classroom')),
            ],
            options={
                'verbose_name_plural': '3. Apps',
                'ordering': ['order'],
            },
        ),
    ]
