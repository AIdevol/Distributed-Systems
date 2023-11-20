# Generated by Django 4.2.7 on 2023-11-09 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("UserModel", "0003_tattowaiver"),
    ]

    operations = [
        migrations.AddField(
            model_name="tattowaiver",
            name="body_location",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="UserModel.tattoo",
            ),
        ),
        migrations.CreateModel(
            name="ToothGemsWaiver",
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
                ("client_name", models.CharField(max_length=255)),
                ("age_initials", models.BooleanField(default=False)),
                ("mental_medical_initials", models.BooleanField(default=False)),
                ("care_instructions_initials", models.BooleanField(default=False)),
                ("colors_variability_initials", models.BooleanField(default=False)),
                ("release_of_liability_initials", models.BooleanField(default=False)),
                ("hold_harmless_initials", models.BooleanField(default=False)),
                ("damages_and_injuries_initials", models.BooleanField(default=False)),
                ("permanent_change_initials", models.BooleanField(default=False)),
                ("tattoo_removal_caution_initials", models.BooleanField(default=False)),
                (
                    "consent_for_photographs_initials",
                    models.BooleanField(default=False),
                ),
                ("infection_information_initials", models.BooleanField(default=False)),
                (
                    "consent_for_communication_initials",
                    models.BooleanField(default=False),
                ),
                ("information_is_true_initials", models.BooleanField(default=False)),
                ("signature_file", models.FileField(upload_to="signatures/")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "body_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserModel.toothgems",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TattoremovalWaiver",
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
                ("client_name", models.CharField(max_length=255)),
                ("age_initials", models.BooleanField(default=False)),
                ("mental_medical_initials", models.BooleanField(default=False)),
                ("care_instructions_initials", models.BooleanField(default=False)),
                ("colors_variability_initials", models.BooleanField(default=False)),
                ("release_of_liability_initials", models.BooleanField(default=False)),
                ("hold_harmless_initials", models.BooleanField(default=False)),
                ("damages_and_injuries_initials", models.BooleanField(default=False)),
                ("permanent_change_initials", models.BooleanField(default=False)),
                ("tattoo_removal_caution_initials", models.BooleanField(default=False)),
                (
                    "consent_for_photographs_initials",
                    models.BooleanField(default=False),
                ),
                ("infection_information_initials", models.BooleanField(default=False)),
                (
                    "consent_for_communication_initials",
                    models.BooleanField(default=False),
                ),
                ("information_is_true_initials", models.BooleanField(default=False)),
                ("signature_file", models.FileField(upload_to="signatures/")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "body_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserModel.tattooremoval",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SMPWaiver",
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
                ("client_name", models.CharField(max_length=255)),
                ("age_initials", models.BooleanField(default=False)),
                ("mental_medical_initials", models.BooleanField(default=False)),
                ("care_instructions_initials", models.BooleanField(default=False)),
                ("colors_variability_initials", models.BooleanField(default=False)),
                ("release_of_liability_initials", models.BooleanField(default=False)),
                ("hold_harmless_initials", models.BooleanField(default=False)),
                ("damages_and_injuries_initials", models.BooleanField(default=False)),
                ("permanent_change_initials", models.BooleanField(default=False)),
                ("tattoo_removal_caution_initials", models.BooleanField(default=False)),
                (
                    "consent_for_photographs_initials",
                    models.BooleanField(default=False),
                ),
                ("infection_information_initials", models.BooleanField(default=False)),
                (
                    "consent_for_communication_initials",
                    models.BooleanField(default=False),
                ),
                ("information_is_true_initials", models.BooleanField(default=False)),
                ("signature_file", models.FileField(upload_to="signatures/")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "body_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="UserModel.smp"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PiercingWaiver",
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
                ("client_name", models.CharField(max_length=255)),
                ("age_initials", models.BooleanField(default=False)),
                ("mental_medical_initials", models.BooleanField(default=False)),
                ("care_instructions_initials", models.BooleanField(default=False)),
                ("colors_variability_initials", models.BooleanField(default=False)),
                ("release_of_liability_initials", models.BooleanField(default=False)),
                ("hold_harmless_initials", models.BooleanField(default=False)),
                ("damages_and_injuries_initials", models.BooleanField(default=False)),
                ("permanent_change_initials", models.BooleanField(default=False)),
                ("tattoo_removal_caution_initials", models.BooleanField(default=False)),
                (
                    "consent_for_photographs_initials",
                    models.BooleanField(default=False),
                ),
                ("infection_information_initials", models.BooleanField(default=False)),
                (
                    "consent_for_communication_initials",
                    models.BooleanField(default=False),
                ),
                ("information_is_true_initials", models.BooleanField(default=False)),
                ("signature_file", models.FileField(upload_to="signatures/")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "body_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserModel.bodylocationpiercing",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PermanentMakeUpWaiver",
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
                ("client_name", models.CharField(max_length=255)),
                ("age_initials", models.BooleanField(default=False)),
                ("mental_medical_initials", models.BooleanField(default=False)),
                ("care_instructions_initials", models.BooleanField(default=False)),
                ("colors_variability_initials", models.BooleanField(default=False)),
                ("release_of_liability_initials", models.BooleanField(default=False)),
                ("hold_harmless_initials", models.BooleanField(default=False)),
                ("damages_and_injuries_initials", models.BooleanField(default=False)),
                ("permanent_change_initials", models.BooleanField(default=False)),
                ("tattoo_removal_caution_initials", models.BooleanField(default=False)),
                (
                    "consent_for_photographs_initials",
                    models.BooleanField(default=False),
                ),
                ("infection_information_initials", models.BooleanField(default=False)),
                (
                    "consent_for_communication_initials",
                    models.BooleanField(default=False),
                ),
                ("information_is_true_initials", models.BooleanField(default=False)),
                ("signature_file", models.FileField(upload_to="signatures/")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "body_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserModel.permanentmakeup",
                    ),
                ),
            ],
        ),
    ]