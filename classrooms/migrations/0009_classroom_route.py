# Generated by Django 3.1.3 on 2020-11-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0008_app_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='route',
            field=models.CharField(default='meet', editable=False, max_length=20),
        ),
    ]