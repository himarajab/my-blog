# Generated by Django 3.0.4 on 2020-07-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200717_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_ar',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]