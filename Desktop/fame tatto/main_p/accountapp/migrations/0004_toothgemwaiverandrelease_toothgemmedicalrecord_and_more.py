# Generated by Django 4.2.6 on 2023-10-16 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accountapp", "0003_rename_city_doctorinfo_city_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ToothGemWaiverAndRelease",
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
                ("age_verification", models.BooleanField(default=False)),
                ("no_impairment", models.BooleanField(default=False)),
                ("tooth_gem_care_agreement", models.BooleanField(default=False)),
                ("release_of_responsibility", models.BooleanField(default=False)),
                ("hold_harmless_agreement", models.BooleanField(default=False)),
                ("damages_responsibility", models.BooleanField(default=False)),
                ("permanent_change_acknowledgment", models.BooleanField(default=False)),
                ("media_authorization", models.BooleanField(default=False)),
                ("infection_acknowledgment", models.BooleanField(default=False)),
                ("text_email_consent", models.BooleanField(default=False)),
                ("real_flat_tooth", models.BooleanField(default=False)),
                ("synthetic_tooth", models.BooleanField(default=False)),
                ("tooth_gem_placement", models.BooleanField(default=False)),
                ("adhesive_wear_off", models.BooleanField(default=False)),
                ("non_permanent_nature", models.BooleanField(default=False)),
                ("professional_removal", models.BooleanField(default=False)),
                ("residual_adhesive", models.BooleanField(default=False)),
                ("teeth_whitening", models.BooleanField(default=False)),
                ("sworn_confirmation", models.BooleanField(default=False)),
                (
                    "service_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accountapp.servicecategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tooth_gem_waiver_and_release",
                        to="accountapp.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ToothGemMedicalRecord",
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
                ("influence_alcohol_drugs", models.BooleanField(default=False)),
                ("allergies", models.BooleanField(default=False)),
                ("medical_skin_conditions", models.BooleanField(default=False)),
                ("communicable_diseases", models.BooleanField(default=False)),
                ("health_conditions", models.BooleanField(default=False)),
                ("sensitive_teeth", models.BooleanField(default=False)),
                ("synthetic_teeth", models.BooleanField(default=False)),
                (
                    "service_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accountapp.servicecategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tooth_gem_medical_records",
                        to="accountapp.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TermAndConditions",
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
                (
                    "service_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accountapp.servicecategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="terms_of_service",
                        to="accountapp.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TattooRemovalWaiverAndRelease",
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
                ("age_verification", models.BooleanField(default=False)),
                ("no_impairment", models.BooleanField(default=False)),
                ("release_of_responsibility", models.BooleanField(default=False)),
                ("hold_harmless_agreement", models.BooleanField(default=False)),
                ("damages_responsibility", models.BooleanField(default=False)),
                ("media_authorization", models.BooleanField(default=False)),
                ("no_other_removal_treatments", models.BooleanField(default=False)),
                ("procedure_discomfort", models.BooleanField(default=False)),
                ("infection_acknowledgment", models.BooleanField(default=False)),
                ("permanent_change_acknowledgment", models.BooleanField(default=False)),
                ("risk_acknowledgment", models.BooleanField(default=False)),
                (
                    "treatment_outcome_acknowledgment",
                    models.BooleanField(default=False),
                ),
                ("text_email_consent", models.BooleanField(default=False)),
                ("sworn_confirmation", models.BooleanField(default=False)),
                (
                    "service_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accountapp.servicecategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tattoo_removal_waiver_and_release",
                        to="accountapp.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TattooRemovalMedicalRecord",
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
                ("tattoo_age", models.PositiveIntegerField()),
                ("adverse_reactions", models.BooleanField(default=False)),
                ("additional_treatment", models.BooleanField(default=False)),
                ("previous_removal_sessions", models.BooleanField(default=False)),
                ("removal_treatment_type", models.CharField(max_length=255)),
                ("total_sessions", models.PositiveIntegerField()),
                ("last_session_date", models.DateField()),
                ("pregnant_nursing", models.BooleanField(default=False)),
                ("hemophiliac_meds", models.BooleanField(default=False)),
                ("medical_skin_conditions", models.CharField(max_length=255)),
                ("communicable_diseases", models.CharField(max_length=255)),
                ("influence_alcohol_drugs", models.BooleanField(default=False)),
                ("allergies", models.CharField(max_length=255)),
                ("health_conditions", models.CharField(max_length=255)),
                ("accutane_usage", models.BooleanField(default=False)),
                ("anesthetic_problems", models.BooleanField(default=False)),
                ("medical_implants", models.BooleanField(default=False)),
                ("asthma", models.BooleanField(default=False)),
                ("autoimmune_disorder", models.BooleanField(default=False)),
                ("faint_dizzy", models.BooleanField(default=False)),
                ("healing_problems", models.BooleanField(default=False)),
                ("herbal_supplements_today", models.BooleanField(default=False)),
                ("hyper_hypo_pigment", models.BooleanField(default=False)),
                ("pacemaker", models.BooleanField(default=False)),
                ("radiation_chemo_treatment", models.BooleanField(default=False)),
                ("seizure_condition", models.BooleanField(default=False)),
                ("skin_cancer", models.BooleanField(default=False)),
                ("smoker", models.BooleanField(default=False)),
                ("tanning_bed_usage", models.BooleanField(default=False)),
                ("sunburn_easily", models.BooleanField(default=False)),
                ("vitiligo", models.BooleanField(default=False)),
                (
                    "service_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accountapp.servicecategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tattoo_removal_medical_records",
                        to="accountapp.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PiercingWaiverAndRelease",
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
                ("age_verification", models.BooleanField(default=False)),
                ("no_impairment", models.BooleanField(default=False)),
                ("piercing_care_agreement", models.BooleanField(default=False)),
                ("release_of_responsibility", models.BooleanField(default=False)),
                ("hold_harmless_agreement", models.BooleanField(default=False)),
                ("damages_responsibility", models.BooleanField(default=False)),
                ("permanent_change_acknowledgment", models.BooleanField(default=False)),
                ("media_authorization", models.BooleanField(default=False)),
                ("infection_acknowledgment", models.BooleanField(default=False)),
                ("text_email_consent", models.BooleanField(default=False)),
                ("sworn_confirmation", models.BooleanField(default=False)),
                (
                    "service_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accountapp.servicecategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="piercing_waiver_and_release",
                        to="accountapp.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PiercingMedicalRecord",
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
                ("pierced_before", models.BooleanField(default=False)),
                ("pregnant_nursing", models.BooleanField(default=False)),
                ("hemophiliac_meds", models.BooleanField(default=False)),
                ("medical_skin_conditions", models.BooleanField(default=False)),
                ("communicable_diseases", models.BooleanField(default=False)),
                ("influence_alcohol_drugs", models.BooleanField(default=False)),
                ("allergies", models.BooleanField(default=False)),
                ("health_conditions", models.BooleanField(default=False)),
                (
                    "service_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accountapp.servicecategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="piercing_medical_records",
                        to="accountapp.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HoldHarmlessAgreement",
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
                ("patron_release_agreement", models.BooleanField(default=False)),
                ("client_photo", models.ImageField(upload_to="client_photos/")),
                (
                    "service_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accountapp.servicecategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hold_harmless_release_agreements",
                        to="accountapp.user",
                    ),
                ),
            ],
        ),
    ]
