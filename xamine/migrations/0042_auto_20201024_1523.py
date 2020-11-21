# Generated by Django 3.1.2 on 2020-10-24 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xamine', '0041_auto_20201023_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patient',
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email_info',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
