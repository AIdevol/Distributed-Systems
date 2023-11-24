# Generated by Django 4.2.4 on 2023-11-21 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("CustomUser", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GuardianDetails",
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
                ("guardian_name", models.CharField(max_length=255)),
                ("guardian_phone", models.CharField(max_length=20)),
                ("guardian_address", models.CharField(max_length=255)),
                ("guardian_email", models.EmailField(max_length=254)),
                ("gaurdian_city", models.CharField(max_length=225)),
                ("gaurdian_state", models.CharField(max_length=250)),
                ("zip_code", models.CharField(max_length=10)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("race", models.CharField(max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="guardian_details",
                        to="CustomUser.customuser",
                    ),
                ),
            ],
        ),
    ]
