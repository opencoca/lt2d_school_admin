# Generated by Django 3.1.4 on 2020-12-08 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20201208_0917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snap',
            old_name='videofile',
            new_name='file',
        ),
    ]