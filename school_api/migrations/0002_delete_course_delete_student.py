# Generated by Django 4.2.5 on 2023-10-03 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
