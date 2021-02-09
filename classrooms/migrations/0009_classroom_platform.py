# Generated by Django 3.1.4 on 2021-02-09 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0008_auto_20210209_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='platform',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classrooms.platform'),
            preserve_default=False,
        ),
    ]
