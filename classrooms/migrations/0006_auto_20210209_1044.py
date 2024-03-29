# Generated by Django 3.1.4 on 2021-02-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0005_auto_20201120_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('iframe', models.URLField()),
                ('logo', models.URLField()),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '4. Meeting Service',
                'ordering': ['order'],
            },
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['classroom__order'], 'verbose_name_plural': '0. Rooms'},
        ),
    ]
