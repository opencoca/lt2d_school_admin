# Generated by Django 3.1.3 on 2020-11-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0003_auto_20201112_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='meet',
            field=models.SlugField(max_length=80),
        ),
    ]
