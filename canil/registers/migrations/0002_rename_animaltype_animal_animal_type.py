# Generated by Django 5.0 on 2023-12-12 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='animalType',
            new_name='animal_type',
        ),
    ]