# Generated by Django 4.1 on 2022-10-26 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_forumpost_rename_content_comment_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpost',
            name='slug',
        ),
    ]