# Generated by Django 3.2.8 on 2021-11-21 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='cancel_date',
            field=models.DateTimeField(null=True),
        ),
    ]
