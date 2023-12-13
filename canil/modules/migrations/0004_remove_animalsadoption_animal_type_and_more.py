# Generated by Django 5.0 on 2023-12-12 22:11

import canil.modules.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_animalsadoption_delete_adoption'),
        ('registers', '0002_rename_animaltype_animal_animal_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalsadoption',
            name='animal_type',
        ),
        migrations.RemoveField(
            model_name='animalsadoption',
            name='greed',
        ),
        migrations.RemoveField(
            model_name='animalsadoption',
            name='name',
        ),
        migrations.AddField(
            model_name='animalsadoption',
            name='animals',
            field=models.ManyToManyField(to='registers.animal'),
        ),
    ]
