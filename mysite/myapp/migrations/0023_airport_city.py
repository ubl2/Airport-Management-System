# Generated by Django 3.2.8 on 2021-11-21 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_tickets_cancel_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport_City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_name', models.CharField(max_length=30)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.city')),
            ],
        ),
    ]
