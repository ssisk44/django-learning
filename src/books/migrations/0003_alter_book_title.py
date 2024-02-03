# Generated by Django 5.0.1 on 2024-02-03 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_book_id_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.booktitle'),
        ),
    ]