# Generated by Django 3.0.4 on 2020-09-18 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0009_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id']},
        ),
    ]
