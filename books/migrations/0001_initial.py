# Generated by Django 3.1.2 on 2020-10-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=10)),
                ('member_type', models.CharField(max_length=10)),
                ('joining_date', models.DateField()),
                ('no_of_issued_books', models.IntegerField()),
            ],
        ),
    ]
