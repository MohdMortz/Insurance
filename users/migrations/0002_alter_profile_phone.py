# Generated by Django 4.0.1 on 2023-01-09 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, max_length=12, null=True, verbose_name=' تلفن ثابت'),
        ),
    ]