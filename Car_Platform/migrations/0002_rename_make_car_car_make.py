# Generated by Django 4.2.2 on 2023-08-08 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Car_Platform", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="make",
            new_name="car_make",
        ),
    ]
