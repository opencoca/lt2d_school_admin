# Generated by Django 3.1.3 on 2020-11-21 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='timestamp',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]