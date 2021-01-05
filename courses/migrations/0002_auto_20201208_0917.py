# Generated by Django 3.1.4 on 2020-12-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='lession',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='syllabus',
            options={'ordering': ['order'], 'verbose_name_plural': 'Syllabus'},
        ),
        migrations.AlterField(
            model_name='snap',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='snap',
            name='videofile',
            field=models.FileField(null=True, upload_to='snap/%Y/%m/%d/', verbose_name=''),
        ),
    ]