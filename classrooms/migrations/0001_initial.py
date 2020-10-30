# Generated by Django 3.1.2 on 2020-10-04 13:20

import classrooms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('breakout_rooms', classrooms.models.IntegerRangeField()),
                ('my_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('classes', models.ManyToManyField(to='classrooms.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('iframe', models.URLField()),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('classes', models.ManyToManyField(to='classrooms.Classroom')),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
    ]