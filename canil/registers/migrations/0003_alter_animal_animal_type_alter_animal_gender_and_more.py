# Generated by Django 5.0 on 2023-12-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0002_rename_animaltype_animal_animal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal_type',
            field=models.CharField(choices=[('A', 'Ape'), ('B', 'Bird'), ('C', 'Cat'), ('D', 'Dog')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='animal',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='animal',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('B', 'Big')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='animal',
            name='status',
            field=models.CharField(choices=[('F', 'Free'), ('H', 'Has Owner'), ('I', 'Ill'), ('D', 'Dead')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(default='São Paulo', max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(default='SP', max_length=2),
        ),
        migrations.AlterField(
            model_name='owner',
            name='city',
            field=models.CharField(default='São Paulo', max_length=200),
        ),
        migrations.AlterField(
            model_name='owner',
            name='state',
            field=models.CharField(default='SP', max_length=2),
        ),
    ]
