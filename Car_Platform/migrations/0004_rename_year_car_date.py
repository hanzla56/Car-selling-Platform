# Generated by Django 4.2.2 on 2023-08-08 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Car_Platform", "0003_car_year"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="year",
            new_name="date",
        ),
    ]
