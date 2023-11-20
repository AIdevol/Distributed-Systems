from django.db import models

class user(models.Model):
    username=models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.CharField(max_length=31, blank=True)
    dob=models.DateField(blank=True)
    save_time=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=30, blank=True)
    GENDER_FIELD=[
        ("M","Male"),
        ("F","Female"),
        ("O", "Others"),
    ]
    gender=models.CharField(max_length=30, choices=GENDER_FIELD)
    race=models.CharField(max_length=30, blank=True)
    
    #if client is the minor fill the details.
    is_minor = models.BooleanField(default=False)
    minor_address = models.CharField(max_length=150, blank=True)
    minor_city = models.CharField(max_length=150, blank=True)
    minor_state = models.CharField(max_length=150, blank=True)
    minor_zip = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.username
    
class ParentDetails(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    parent_address = models.CharField(max_length=150)
    parent_city = models.CharField(max_length=150)
    parent_state = models.CharField(max_length=150)
    parent_zip = models.CharField(max_length=10)

    def __str__(self):
        return self.parent_name

class userdetails(models.Model):
    address=models.CharField(max_length=150, blank=True)
    state=models.CharField(max_length=150, blank= True)
    zip=models.CharField(max_length=10)
    city=models.CharField(max_length=150, blank=True)
    country=models.CharField(max_length=50, blank=True)


class ServiceCategory(models.Model):
    category_choices=[
        ("tattoo","Tattoo"),
        ("piercing","Piercing"),
        ("toothe gems", "Toothe Gems"),
        ("tattoo removal", "Tattoo Removal"),
        ("permanent makeup", "Permanent Makeup"),
        ("smp", "Scalp Micro-Pigmentation"),
    ]

    #category=models.CharField(max_length=30)
    selected_Cotegory=models.CharField(max_length=21, choices=category_choices, blank=True, null=False)


    def __str__(self):
        return self.selected_Cotegory


class User_selected_category(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE, related_name='select_services')
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)


class SharedMedicalRecord(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE,related_name='Medical_Record')
    Tattoo_before=models.BooleanField(default=False)
    Pregnanancy_conditions=models.BooleanField(default=False)
    Hemophiliac_attention=models.BooleanField(default=False)
    Medical_or_skin_condition=models.BooleanField(default=False)
    Communicable_disease=models.BooleanField(default=False)
    Influence_drug_alcohol=models.BooleanField(default=False)
    Heart_disease=models.BooleanField(default=False)

class Emergency_Contact(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE, related_name='Emergency_Contact')
    Name=models.CharField(max_length=150, blank=True)
    Phone_number=models.CharField(max_length=20, blank=True)
    City=models.CharField(max_length= 200, blank= True)
    State=models.CharField(max_length=150, blank=True)

class DoctorInfo(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE, related_name="Doctor_Informations")
    Name=models.CharField(max_length=50, blank=True)
    Phone_number=models.CharField(max_length=20)
    City=models.CharField(max_length=200,blank=True)
    State=models.CharField(max_length=150, blank=True)

class SharedWaiverAndRelease(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="waiver_and_release")
    # Age_verification = models.BooleanField(default=False)
    # No_impairment = models.BooleanField(default=False)
    page_1 = models.BooleanField(default=False)
    page_2 = models.BooleanField(default=False)
    page_3 = models.BooleanField(default=False)
    page_4 = models.BooleanField(default=False)
    page_5 = models.BooleanField(default=False)
    page_6 = models.BooleanField(default=False)


class HoldHarmlessAgreement(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="hold_harmless_release_agreements")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    patron_release_agreement = models.BooleanField(default=False)
    client_photo = models.ImageField(upload_to="client_photos/", blank= True, null= False)

class PiercingMedicalRecord(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="piercing_medical_records")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    pierced_before = models.BooleanField(default=False)
    pregnant_nursing = models.BooleanField(default=False)
    hemophiliac_meds = models.BooleanField(default=False)
    medical_skin_conditions = models.BooleanField(default=False)
    communicable_diseases = models.BooleanField(default=False)
    influence_alcohol_drugs = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    health_conditions = models.BooleanField(default=False)

class ToothGemMedicalRecord(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="tooth_gem_medical_records")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    influence_alcohol_drugs = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    medical_skin_conditions = models.BooleanField(default=False)
    communicable_diseases = models.BooleanField(default=False)
    health_conditions = models.BooleanField(default=False)
    sensitive_teeth = models.BooleanField(default=False)
    synthetic_teeth = models.BooleanField(default=False)

class TattooRemovalMedicalRecord(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="tattoo_removal_medical_records")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    tattoo_age = models.PositiveIntegerField()
    adverse_reactions = models.BooleanField(default=False)
    additional_treatment = models.BooleanField(default=False)
    previous_removal_sessions = models.BooleanField(default=False)
    removal_treatment_type = models.CharField(max_length=255)
    total_sessions = models.PositiveIntegerField()
    last_session_date = models.DateField()
    pregnant_nursing = models.BooleanField(default=False)
    hemophiliac_meds = models.BooleanField(default=False)
    medical_skin_conditions = models.CharField(max_length=255)
    communicable_diseases = models.CharField(max_length=255)
    influence_alcohol_drugs = models.BooleanField(default=False)
    allergies = models.CharField(max_length=255)
    health_conditions = models.CharField(max_length=255)
    accutane_usage = models.BooleanField(default=False)
    anesthetic_problems = models.BooleanField(default=False)
    medical_implants = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    autoimmune_disorder = models.BooleanField(default=False)
    faint_dizzy = models.BooleanField(default=False)
    healing_problems = models.BooleanField(default=False)
    herbal_supplements_today = models.BooleanField(default=False)
    hyper_hypo_pigment = models.BooleanField(default=False)
    pacemaker = models.BooleanField(default=False)
    radiation_chemo_treatment = models.BooleanField(default=False)
    seizure_condition = models.BooleanField(default=False)
    skin_cancer = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)
    tanning_bed_usage = models.BooleanField(default=False)
    sunburn_easily = models.BooleanField(default=False)
    vitiligo = models.BooleanField(default=False)

class PiercingWaiverAndRelease(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="piercing_waiver_and_release")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    age_verification = models.BooleanField(default=False)
    no_impairment = models.BooleanField(default=False)
    piercing_care_agreement = models.BooleanField(default=False)
    release_of_responsibility = models.BooleanField(default=False)
    hold_harmless_agreement = models.BooleanField(default=False)
    damages_responsibility = models.BooleanField(default=False)
    permanent_change_acknowledgment = models.BooleanField(default=False)
    media_authorization = models.BooleanField(default=False)
    infection_acknowledgment = models.BooleanField(default=False)
    text_email_consent = models.BooleanField(default=False)
    sworn_confirmation = models.BooleanField(default=False)

class ToothGemWaiverAndRelease(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="tooth_gem_waiver_and_release")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    age_verification = models.BooleanField(default=False)
    no_impairment = models.BooleanField(default=False)
    tooth_gem_care_agreement = models.BooleanField(default=False)
    release_of_responsibility = models.BooleanField(default=False)
    hold_harmless_agreement = models.BooleanField(default=False)
    damages_responsibility = models.BooleanField(default=False)
    permanent_change_acknowledgment = models.BooleanField(default=False)
    media_authorization = models.BooleanField(default=False)
    infection_acknowledgment = models.BooleanField(default=False)
    text_email_consent = models.BooleanField(default=False)
    real_flat_tooth = models.BooleanField(default=False)
    synthetic_tooth = models.BooleanField(default=False)
    tooth_gem_placement = models.BooleanField(default=False)
    adhesive_wear_off = models.BooleanField(default=False)
    non_permanent_nature = models.BooleanField(default=False)
    professional_removal = models.BooleanField(default=False)
    residual_adhesive = models.BooleanField(default=False)
    teeth_whitening = models.BooleanField(default=False)
    sworn_confirmation = models.BooleanField(default=False)

class TattooRemovalWaiverAndRelease(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="tattoo_removal_waiver_and_release")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    age_verification = models.BooleanField(default=False)
    no_impairment = models.BooleanField(default=False)
    release_of_responsibility = models.BooleanField(default=False)
    hold_harmless_agreement = models.BooleanField(default=False)
    damages_responsibility = models.BooleanField(default=False)
    media_authorization = models.BooleanField(default=False)
    no_other_removal_treatments = models.BooleanField(default=False)
    procedure_discomfort = models.BooleanField(default=False)
    infection_acknowledgment = models.BooleanField(default=False)
    permanent_change_acknowledgment = models.BooleanField(default=False)
    risk_acknowledgment = models.BooleanField(default=False)
    treatment_outcome_acknowledgment = models.BooleanField(default=False)
    text_email_consent = models.BooleanField(default=False)
    sworn_confirmation = models.BooleanField(default=False)


class TermAndConditions(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="terms_of_service")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)