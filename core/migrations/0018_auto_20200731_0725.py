# Generated by Django 3.0.4 on 2020-07-31 07:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_data_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='body',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
            preserve_default=False,
        ),
    ]