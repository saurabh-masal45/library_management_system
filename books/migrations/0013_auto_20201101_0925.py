# Generated by Django 3.1.2 on 2020-11-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20201101_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='return_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
