# Generated by Django 4.2.1 on 2023-06-05 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0003_post_dislikes_post_likes_delete_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]