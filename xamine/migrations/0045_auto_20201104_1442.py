# Generated by Django 3.1.2 on 2020-11-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0044_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AddField(
            model_name='invoice',
            name='isPaid',
            field=models.BooleanField(default=False),
        ),
    ]