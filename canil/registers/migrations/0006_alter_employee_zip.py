# Generated by Django 5.0 on 2023-12-18 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0005_alter_owner_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='zip',
            field=models.CharField(max_length=8),
        ),
    ]
