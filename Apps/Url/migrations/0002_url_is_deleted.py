# Generated by Django 3.2.10 on 2022-02-05 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Url', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is Url Deleted'),
        ),
    ]
