# Generated by Django 3.2 on 2022-06-13 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=260)),
                ('pic', models.ImageField(blank=True, upload_to='profilepics/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('contact', models.CharField(max_length=70)),
                ('projez', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', tinymce.models.HTMLField()),
                ('link', models.CharField(max_length=60)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('projimage', models.ImageField(blank=True, upload_to='articles/')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=85)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moringaawardz.project')),
            ],
        ),
    ]
