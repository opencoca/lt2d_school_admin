# Generated by Django 3.1.2 on 2020-10-14 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0007_auto_20201006_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='logo',
            field=models.URLField(default='https://camp.centrepreville.org/assets/tv.png'),
            preserve_default=False,
        ),
    ]