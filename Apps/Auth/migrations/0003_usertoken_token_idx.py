# Generated by Django 3.2.10 on 2022-02-13 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_alter_usertoken_id'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='usertoken',
            index=models.Index(fields=['token'], name='token_idx'),
        ),
    ]
