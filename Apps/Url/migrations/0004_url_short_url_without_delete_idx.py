# Generated by Django 3.2.10 on 2022-02-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Url', '0003_url_short_url_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='url',
            index=models.Index(fields=['short_url', 'is_deleted'], name='short_url_without_delete_idx'),
        ),
    ]
