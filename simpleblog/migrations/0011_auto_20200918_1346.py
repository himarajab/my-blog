# Generated by Django 3.0.4 on 2020-09-18 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0010_auto_20200918_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]
