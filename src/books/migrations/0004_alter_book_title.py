# Generated by Django 5.0.1 on 2024-02-03 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_books', to='books.booktitle'),
        ),
    ]
