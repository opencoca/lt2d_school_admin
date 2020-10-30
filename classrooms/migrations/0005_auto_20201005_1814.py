# Generated by Django 3.1.2 on 2020-10-05 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0004_auto_20201004_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='classes',
            field=models.ManyToManyField(blank=True, null=True, to='classrooms.Classroom'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='classes',
            field=models.ManyToManyField(blank=True, null=True, to='classrooms.Classroom'),
        ),
    ]
