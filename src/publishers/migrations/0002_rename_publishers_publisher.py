# Generated by Django 5.0.1 on 2024-02-01 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publishers',
            new_name='Publisher',
        ),
    ]
