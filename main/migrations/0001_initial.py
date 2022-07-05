# Generated by Django 4.0.6 on 2022-07-05 00:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='webster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(max_length=40)),
                ('Detail', models.TextField()),
                ('image', models.ImageField(default=None, upload_to='post_image')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 5, 1, 5, 7, 789354))),
                ('no_of_likes', models.IntegerField(default=0)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('body', models.TextField()),
                ('Date_added', models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 5, 1, 5, 7, 790355))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.profile')),
            ],
        ),
    ]
