# Generated by Django 5.0.1 on 2024-02-01 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0002_rename_publishers_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='country',
        ),
    ]