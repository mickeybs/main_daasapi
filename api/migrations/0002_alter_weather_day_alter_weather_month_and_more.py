# Generated by Django 4.0.4 on 2022-05-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='day',
            field=models.IntegerField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='month',
            field=models.IntegerField(max_length=64),
        ),
        migrations.AlterField(
            model_name='weather',
            name='rain',
            field=models.DecimalField(decimal_places=2, max_digits=3, unique=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='tmax',
            field=models.DecimalField(decimal_places=2, max_digits=3, unique=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='tmin',
            field=models.DecimalField(decimal_places=2, max_digits=3, unique=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='year',
            field=models.IntegerField(max_length=64),
        ),
    ]
