# Generated by Django 3.1.5 on 2021-01-17 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyApi', '0003_project_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='student_name',
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
