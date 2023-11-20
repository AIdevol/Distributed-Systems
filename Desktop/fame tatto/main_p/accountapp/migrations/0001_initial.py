# Generated by Django 4.2.4 on 2023-10-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ServiceCategory",
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
                ("category", models.CharField(max_length=30)),
                (
                    "selected_Cotegory",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("tattoo", "Tattoo"),
                            ("piercing", "Piercing"),
                            ("toothe gems", "Toothe Gems"),
                            ("tattoo removal", "Tattoo Removal"),
                            ("permanent makeup", "Permanent Makeup"),
                            ("smp", "Scalp Micro-Pigmentation"),
                        ],
                        max_length=21,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="user",
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
                ("username", models.CharField(blank=True, max_length=30)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email", models.CharField(blank=True, max_length=31)),
                ("dob", models.DateField(blank=True)),
                ("save_time", models.DateTimeField(auto_now_add=True)),
                ("phonenumber", models.CharField(blank=True, max_length=30)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        max_length=30,
                    ),
                ),
                ("race", models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="userdetails",
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
                ("address", models.CharField(blank=True, max_length=150)),
                ("state", models.CharField(blank=True, max_length=150)),
                ("zip", models.CharField(max_length=10)),
                ("city", models.CharField(blank=True, max_length=150)),
                ("country", models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
