# Generated by Django 3.2.8 on 2021-11-20 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_state_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state_zipcode',
            name='zip_code',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
