# Generated by Django 5.0.1 on 2024-02-01 21:07

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0004_publisher_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=django_countries.fields.CountryField(max_length=40),
        ),
    ]
