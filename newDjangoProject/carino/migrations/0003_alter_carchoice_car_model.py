# Generated by Django 4.1 on 2022-08-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carino', '0002_carchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carchoice',
            name='car_model',
            field=models.CharField(max_length=50),
        ),
    ]