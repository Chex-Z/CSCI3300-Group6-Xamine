# Generated by Django 3.0.5 on 2020-04-29 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0037_auto_20200429_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='notes',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='report',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='notes',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]