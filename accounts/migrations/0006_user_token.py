# Generated by Django 4.0.1 on 2023-04-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, editable=False, max_length=32, null=True),
        ),
    ]
