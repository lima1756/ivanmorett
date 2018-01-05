# Generated by Django 2.0 on 2018-01-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180103_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['visible', '-date_published', '-date_time_modification']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_time_published',
        ),
        migrations.AddField(
            model_name='post',
            name='date_published',
            field=models.DateField(null=True, verbose_name='Published Date'),
        ),
    ]
