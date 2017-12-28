# Generated by Django 2.0 on 2017-12-28 03:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('date_time_published', models.DateTimeField(auto_now=True, verbose_name='Publication date-time')),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(help_text='This is only for stadistics, it will not be shared', max_length=254)),
                ('answer_to', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Comment')),
            ],
            options={
                'ordering': ['-date_time_published'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date-time')),
                ('date_time_modification', models.DateTimeField(auto_now=True, verbose_name='Modification Date-time')),
                ('date_time_published', models.DateTimeField(verbose_name='Date-time of publication')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('claps', models.BigIntegerField(default=0, help_text="This is a representation of how much is liked the post, if you like it much you can give a lot of claps, if you don't you don't give any clap")),
                ('visible', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date_time_published', '-date_time_modification'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
