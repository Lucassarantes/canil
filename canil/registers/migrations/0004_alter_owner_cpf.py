# Generated by Django 5.0 on 2023-12-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0003_alter_animal_animal_type_alter_animal_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]