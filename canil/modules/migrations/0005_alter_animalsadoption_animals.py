# Generated by Django 5.0 on 2023-12-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_remove_animalsadoption_animal_type_and_more'),
        ('registers', '0002_rename_animaltype_animal_animal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalsadoption',
            name='animals',
            field=models.ManyToManyField(to='registers.animal'),
        ),
    ]