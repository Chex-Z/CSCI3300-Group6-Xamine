# Generated by Django 3.0.5 on 2020-04-19 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xamine', '0027_order_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='doctor',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
