# Generated by Django 4.0.1 on 2023-05-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='token',
        ),
        migrations.AddField(
            model_name='post',
            name='viewers',
            field=models.IntegerField(default=0),
        ),
    ]
