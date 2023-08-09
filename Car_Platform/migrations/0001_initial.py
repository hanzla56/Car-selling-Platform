# Generated by Django 4.2.2 on 2023-08-08 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car_make",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="")),
                ("price", models.IntegerField()),
                ("km_driven", models.FloatField()),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("like_new", "Like New"),
                            ("excellent", "Excellent"),
                            ("good", "Good"),
                            ("fair", "Fair"),
                            ("poor", "Poor"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "transmission",
                    models.CharField(
                        choices=[("automatic", "Automatic"), ("manual", "Manual")],
                        max_length=30,
                    ),
                ),
                ("owner_name", models.CharField(max_length=50)),
                ("owner_email", models.EmailField(max_length=254)),
                ("owner_contact", models.IntegerField()),
                (
                    "make",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Car_Platform.car_make",
                    ),
                ),
            ],
        ),
    ]