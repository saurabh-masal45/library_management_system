# Generated by Django 3.1.2 on 2020-10-21 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_book_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='author',
        ),
        migrations.DeleteModel(
            name='member',
        ),
    ]
