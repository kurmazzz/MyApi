# Generated by Django 3.1.5 on 2021-01-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApi', '0005_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, default='2020-01-01'),
        ),
    ]
