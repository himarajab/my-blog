# Generated by Django 3.0.4 on 2020-07-12 02:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200711_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='body_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
    ]
