# Generated by Django 3.2.8 on 2021-11-20 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_airport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_code',
            fields=[
                ('airline_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
    ]
