# Generated by Django 4.0.1 on 2022-11-01 22:20

import uuid

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1, verbose_name='وضعیت')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subscriber', models.EmailField(max_length=128, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='ایمیل')),
            ],
            options={
                'verbose_name': 'خبر نامه',
                'verbose_name_plural': 'خبر نامه ها',
                'ordering': ['subscriber'],
            },
        ),
        migrations.CreateModel(
            name='ScheduleMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='موضوع')),
                ('content', models.TextField(max_length=3000, verbose_name='پیام')),
            ],
            options={
                'verbose_name': 'برنامه ایمیل',
                'verbose_name_plural': 'برنامه ایمیل',
                'ordering': ['-created'],
            },
        ),
    ]
