# Generated by Django 3.1.3 on 2020-11-21 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0002_auto_20201120_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['slug']},
        ),
        migrations.RemoveField(
            model_name='video',
            name='timestamp',
        ),
    ]