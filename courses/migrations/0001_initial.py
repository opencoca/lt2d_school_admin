# Generated by Django 3.1.3 on 2020-12-04 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '2. Lessions',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '0. Syllabus',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('syllabus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='courses.syllabus')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '1. Course',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Snap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtile', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('slug', models.SlugField(unique=True)),
                ('videofile', models.FileField(null=True, upload_to='videos/%Y/%m/%d/', verbose_name='')),
                ('page', models.ManyToManyField(blank=True, to='courses.Lession')),
            ],
            options={
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('lession', models.ManyToManyField(blank=True, to='courses.Lession')),
            ],
            options={
                'verbose_name_plural': '2. Pages',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='lession',
            name='course',
            field=models.ManyToManyField(blank=True, to='courses.Course'),
        ),
    ]
