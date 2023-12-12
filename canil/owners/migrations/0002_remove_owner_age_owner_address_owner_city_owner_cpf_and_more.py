# Generated by Django 5.0 on 2023-12-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='age',
        ),
        migrations.AddField(
            model_name='owner',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='city',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='cpf',
            field=models.CharField(default=3, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='state',
            field=models.CharField(default=4, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='zip',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Animal',
        ),
    ]
