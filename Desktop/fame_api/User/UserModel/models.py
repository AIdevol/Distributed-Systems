from django.db import models

class ServiceCategories(models.Model):
    TATTOO = "tattoo"
    PIERCING = "piercing"
    TOOTH_GEMS = "tooth_gems"
    TATTOO_REMOVAL = "tattoo_removal"
    PERMANENT_MAKEUP = "permanent_makeup"
    SCALP_MICRO_PIGMENTATION = "scalp_micro_pigmentation"

    CHOICES = [
        (TATTOO, "Tattoo"),
        (PIERCING, "Piercing"),
        (TOOTH_GEMS, "Tooth Gems"),
        (TATTOO_REMOVAL, "Tattoo Removal"),
        (PERMANENT_MAKEUP, "Permanent Makeup"),
        (SCALP_MICRO_PIGMENTATION, "Scalp Micro-Pigmentation"),
    ]

    name = models.CharField(max_length=100, choices=CHOICES)

    def __str__(self):
        return self.name


class UserService(models.Model):
    service_name = models.CharField(max_length=100)
    service_categories = models.ForeignKey(
        ServiceCategories, on_delete=models.CASCADE, related_name="services"
    )

    def __str__(self):
        return self.service_name

class Tattoo(models.Model):
    body_location=models.ForeignKey(ServiceCategories, on_delete=models.CASCADE)
    Name=models.CharField(max_length= 30)
    Parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.Name
    
class BodyLocation(models.Model):
    HEAD = "head"
    NECK = "neck"
    CHEST = "chest"
    TORSO = "torso"
    BACK = "back"
    ARM = "arm"
    HAND = "hand"
    HIP = "hip"
    GLUTES = "glutes"
    PELVIC = "pelvic"
    LEG = "leg"
    FOOT = "foot"

    name = models.CharField(
        max_length=100,
        choices=[
            (HEAD, "Head"),
            (NECK, "Neck"),
            (CHEST, "Chest"),
            (TORSO, "Torso"),
            (BACK, "Back"),
            (ARM, "Arm"),
            (HAND, "Hand"),
            (HIP, "Hip"),
            (GLUTES, "Glutes"),
            (PELVIC, "Pelvic"),
            (LEG, "Leg"),
            (FOOT, "Foot"),
        ],
    )
    service_categories = models.ForeignKey(
        ServiceCategories, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Head(models.Model):
    body_location = models.ForeignKey(BodyLocation, on_delete=models.CASCADE)
    Face=models.BooleanField(default=False)
    Scalp= models.BooleanField(default=False)
    Ear=models.BooleanField(default=False)

class Neck(models.Model):
    body_location=models.ForeignKey(BodyLocation,on_delete=models.CASCADE)
    Full_Chest=models.BooleanField(default=False)
    Left_side=models.BooleanField(default= False)
    Right_side=models.BooleanField(default=False)
    Center=models.BooleanField(default=False)
    Collarbone=models.BooleanField(default= False)
    Nipple=models.BooleanField(default=False)
    Under_chest=models.BooleanField(default=False)

class Nipple(models.Model):
    body_location=models.ForeignKey(Neck, on_delete=models.CASCADE)
    Left=models.BooleanField(default=False)
    Right=models.BooleanField(default=False)

class Under_chest(models.Model):
    body_location=models.ForeignKey(Neck, on_delete=models.CASCADE)
    Left=models.BooleanField(default=False)
    Right=models.BooleanField(default=False)

class Face(models.Model):
    body_location = models.ForeignKey(Head, on_delete=models.CASCADE)
    Forehead = models.BooleanField(default=False)
    Temple = models.BooleanField(default=False)
    Eye_Brow = models.BooleanField(default=False)
    Eyelid = models.BooleanField(default=False)
    Nose = models.BooleanField(default=False)
    Cheeks = models.BooleanField(default=False)
    Lip= models.BooleanField(default=False)
    Jaw = models.BooleanField(default=False)

class Forehead(models.Model):
    body_location = models.ForeignKey(Face,on_delete=models.CASCADE)
    Left=models.BooleanField(default=False)
    Right=models.BooleanField(default=False)
    center=models.BooleanField(default=False)

class Temple(models.Model):
    body_location = models.ForeignKey(Face,on_delete=models.CASCADE)
    Left=models.BooleanField(default=False)
    Right=models.BooleanField(default=False)

class Eye_Brow(models.Model):
    body_location = models.ForeignKey(Face,on_delete=models.CASCADE)
    Left=models.BooleanField(default=False)
    Right=models.BooleanField(default=False)

class Eyelid(models.Model):
    body_location = models.ForeignKey(Face,on_delete=models.CASCADE)
    Left=models.BooleanField(default=False)
    Right=models.BooleanField(default=False)

class Nose(models.Model):
    body_location = models.ForeignKey(Face,on_delete=models.CASCADE)

class Cheeks(models.Model):
    body_location = models.ForeignKey(Face,on_delete=models.CASCADE)
    Left=models.BooleanField(default=False)
    Right=models.BooleanField(default=False)

class Lip(models.Model):
    body_location = models.ForeignKey(Face,on_delete=models.CASCADE)
    Upper_Lip=models.BooleanField(default=False)
    Lower_Lip=models.BooleanField(default=False)

class Jaw(models.Model):
    body_location = models.ForeignKey(Face,on_delete=models.CASCADE)
    Left=models.BooleanField(default=False)
    Right=models.BooleanField(default=False)
    Chin =models.BooleanField(default=False)

class Scalp(models.Model):
    body_location = models.ForeignKey(Head, on_delete=models.CASCADE)

    SCALP_PART_CHOICES = [
        ('top', 'Top'),
        ('back', 'Back'),
        ('left', 'Left'),
        ('full', 'Full'),
    ]

    scalp_parts = models.CharField(
        max_length=10,
        choices=SCALP_PART_CHOICES,
        default='full' 
    )   

    def __str__(self):
        return self.get_scalp_parts_display()

class Ear(models.Model):
    Body_location = models.ForeignKey(Head, on_delete=models.CASCADE)
    Right_Ear = models.BooleanField(default=False)
    RIGHT_EAR_PART_CHOICES = [
        ('behind', 'Behind'),
        ('inner', 'Inner'),
        ('lobe', 'Lobe'),
    ]
    right_ear_parts = models.CharField(
        max_length=10,
        choices=RIGHT_EAR_PART_CHOICES,
        default='lobe'
    )

    Left_Ear = models.BooleanField(default=False)
    LIGHT_EAR_PART_CHOICES = [
        ('behind', 'Behind'),
        ('inner', 'Inner'),
        ('lobe', 'Lobe'),
    ]
    left_ear_parts = models.CharField(
        max_length=10,
        choices=RIGHT_EAR_PART_CHOICES,
        default='lobe'
    )
    def __str__(self):
        return self.get_right_ear_parts_display()
    
class Torso(models.Model):
    body_location=models.ForeignKey(BodyLocation,on_delete=models.CASCADE)
    Full_Torso=models.BooleanField(default=False)
    Left_Ribs=models.BooleanField(default=False)
    Right_Ribs=models.BooleanField(default=False)
    Stomach=models.BooleanField(default=False)
    Belly_Button=models.BooleanField(default=False)
    TummyTuck=models.BooleanField(default=False)

class Back(models.Model):
    body_location=models.ForeignKey(BodyLocation, on_delete=models.CASCADE)
    Full_BackPiece=models.BooleanField(default=False)
    Right_Shoulder=models.BooleanField(default=False)
    Left_Shoulder=models.BooleanField(default=False)
    Spine=models.BooleanField(default=False)
    Lower_Back=models.BooleanField(default=False)
    Other=models.BooleanField(default=False)
    Other_explaination=models.TextField(default=False)

class Arm(models.Model):
    body_location=models.ForeignKey(BodyLocation, on_delete=models.CASCADE)
    Left_Arm=models.BooleanField(default=False)
    LEFT_ARM_CHOICES=[
        ('half shoulder', "Half Sleeve"),
        ("shoulder", "Shoulder"),
        ("armpit", "ArmPit"),
        ("upper armpit inner", "Upper ArmPit - Inner"),
        ("upper armpit outer", "Upper ArmPit - Outer"),
        ("upper armpit front", "Upper ArmPit - Front"),
        ("upper armpit back", "Upper ArmPit - Back"),
        ("elbow", "Elbow-Inner"),
        ("elbow", "Elbow-Outer"),
        ("forearm","Forearm-Inner"),
        ("forearm","Forearm-Outer"),
        ("forearm","Forearm-Side"),
        ('wrist','Wrist-Inner'),
        ('wrist','Wrist-Outer'),
        ('wrist','Wrist-Side'),
    ]
    left_arm_parts = models.CharField(
        max_length=20,
        choices=LEFT_ARM_CHOICES,
        default='ArmPit'
    )


    Right_Arm=models.BooleanField(default=False)
    RIGHT_ARM_CHOICES=[
        ('half shoulder', "Half Sleeve"),
        ("shoulder", "Shoulder"),
        ("armpit", "ArmPit"),
        ("upper armpit inner", "Upper ArmPit - Inner"),
        ("upper armpit outer", "Upper ArmPit - Outer"),
        ("upper armpit front", "Upper ArmPit - Front"),
        ("upper armpit back", "Upper ArmPit - Back"),
        ("elbow", "Elbow-Inner"),
        ("elbow", "Elbow-Outer"),
        ("forearm","Forearm-Inner"),
        ("forearm","Forearm-Outer"),
        ("forearm","Forearm-Side"),
        ('wrist','Wrist-Inner'),
        ('wrist','Wrist-Outer'),
        ('wrist','Wrist-Side'),


    ]
    Right_arm_parts = models.CharField(
        max_length=20,
        choices=RIGHT_ARM_CHOICES,
        default='ArmPit'
    )

class Hand(models.Model):
    body_location=models.ForeignKey(BodyLocation, on_delete=models.CASCADE)
    Left = models.BooleanField(default=False)
    Right = models.BooleanField(default=False)

    # Subparts for the Left Hand
    Left_Top = models.BooleanField(default=False)
    Left_Palm = models.BooleanField(default=False)
    Left_Side = models.BooleanField(default=False)
    Left_Fingers = models.BooleanField(default=False)

    # Subparts for the Right Hand
    Right_Top = models.BooleanField(default=False)
    Right_Palm = models.BooleanField(default=False)
    Right_Side = models.BooleanField(default=False)
    Right_Fingers = models.BooleanField(default=False)

    def __str__(self):
        return "Hand"

class Hip(models.Model):
    body_location=models.ForeignKey(BodyLocation, on_delete=models.CASCADE)
    Left = models.BooleanField(default=False)
    Right = models.BooleanField(default=False)

    def __str__(self):
        return "Hip"

class Glutes(models.Model):
    body_location=models.ForeignKey(BodyLocation, on_delete=models.CASCADE)
    Left = models.BooleanField(default=False)
    Right = models.BooleanField(default=False)

    def __str__(self):
        return "Left"
    
class Pelvic(models.Model):
    body_location=models.ForeignKey(BodyLocation, on_delete=models.CASCADE)
    Top=models.BooleanField(default=False)
    Middle=models.BooleanField(default=False)
    Bottom=models.BooleanField(default=False)
    Left=models.BooleanField(default=False)
    Right=models.BooleanField(default=False)
    Full=models.BooleanField(default=False)

class Leg(models.Model):
    body_location = models.ForeignKey(BodyLocation, on_delete=models.CASCADE)
    Left_Leg = models.BooleanField(default=False)

    # Full Sleeve for Left Leg
    Left_Full_Sleeve = models.BooleanField(default=False)
    LEFT_FULL_SLEEVE_CHOICES = [
        ('lower', 'Lower'),
        ('upper', 'Upper'),
    ]
    Left_Full_Sleeve_Part = models.CharField(
        max_length=10,
        choices=LEFT_FULL_SLEEVE_CHOICES,
        blank=True,
        null=True,
    )

    # Half Sleeve for Left Leg
    Left_Half_Sleeve = models.BooleanField(default=False)
    LEFT_HALF_SLEEVE_CHOICES = [
        ('lower', 'Lower'),
        ('upper', 'Upper'),
    ]
    Left_Half_Sleeve_Part = models.CharField(
        max_length=10,
        choices=LEFT_HALF_SLEEVE_CHOICES,
        blank=True,
        null=True,
    )

    Right_Leg = models.BooleanField(default=False)

    # Full Sleeve for Right Leg
    Full_Right_Leg = models.BooleanField(default=False)
    RIGHT_FULL_SLEEVE_CHOICES = [
        ('lower', 'Lower'),
        ('upper', 'Upper'),
    ]
    Right_Full_Sleeve_Part = models.CharField(
        max_length=10,
        choices=RIGHT_FULL_SLEEVE_CHOICES,
        blank=True,
        null=True,
    )

    # Half Sleeve for Right Leg
    Full_Left_Half_Sleeve = models.BooleanField(default=False)
    LEFT_HALF_SLEEVE_CHOICES = [
        ('lower', 'Lower'),
        ('upper', 'Upper'),
    ]
    Left_Half_Sleeve_Part = models.CharField(
        max_length=10,
        choices=LEFT_HALF_SLEEVE_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return "Leg"


class Thigh(models.Model):
    body_location = models.ForeignKey(Leg, on_delete=models.CASCADE)
    Inner = models.BooleanField(default=False)
    Outer = models.BooleanField(default=False)
    Front = models.BooleanField(default=False)
    Back = models.BooleanField(default=False)

    def __str__(self):
        return "Thigh"

class Knee(models.Model):
    body_location = models.ForeignKey(Leg, on_delete=models.CASCADE)
    Knee = models.BooleanField(default=False)
    Front = models.BooleanField(default=False)
    Back = models.BooleanField(default=False)

    def __str__(self):
        return "Knee"

class LowerLeg(models.Model):
    body_location = models.ForeignKey(Leg, on_delete=models.CASCADE)
    Inner = models.BooleanField(default=False)
    Outer = models.BooleanField(default=False)
    Front = models.BooleanField(default=False)
    Back = models.BooleanField(default=False)

    def __str__(self):
        return "Lower Leg"


class Ankle(models.Model):
    body_location = models.ForeignKey(Leg, on_delete=models.CASCADE)
    Full = models.BooleanField(default=False)
    Inner = models.BooleanField(default=False)
    Outer = models.BooleanField(default=False)
    Front = models.BooleanField(default=False)
    Back = models.BooleanField(default=False)

    def __str__(self):
        return "Ankle"

class Foot(models.Model):
    body_location=models.ForeignKey(BodyLocation, on_delete=models.CASCADE)
    Left=models.BooleanField(default=False)
    Left_Top=models.BooleanField(default=False)
    Left_side=models.BooleanField(default=False)
    Left_Toes=models.BooleanField(default=False)

    Right=models.BooleanField(default=False)
    Right_Top=models.BooleanField(default=False)
    Right_side=models.BooleanField(default=False)
    Right_Toes=models.BooleanField(default=False)

    def __str__(self):
        return "left"

#piercing Models

class BodyLocationPiercing(models.Model):
    body_location=models.ForeignKey(ServiceCategories, on_delete=models.CASCADE)

    BELLY_PIERCING = "Belly Piercing"
    EAR_AREA_PIERCING = "Ear Area Piercing"
    FACIAL_AREA_PIERCING = "Facial Area Piercing"
    JEWELRY_SWAP_PIERCING = "Jewelry Swap Piercing"
    NIPPLE_PIERCING = "Nipple Piercing"
    NOSE_AREA_PIERCING = "Nose Area Piercing"
    ORAL_AREA_PIERCING = "Oral Area Piercing"
    SURFACE_PIERCING = "Surface Piercing"
    VAGINAL_AREA_PIERCING = "Vaginal Area Piercing"

    PIERCING_CATEGORIES = [
        (BELLY_PIERCING, "Belly Piercing"),
        (EAR_AREA_PIERCING, "Ear Area Piercing"),
        (FACIAL_AREA_PIERCING, "Facial Area Piercing"),
        (JEWELRY_SWAP_PIERCING, "Jewelry Swap Piercing"),
        (NIPPLE_PIERCING, "Nipple Piercing"),
        (NOSE_AREA_PIERCING, "Nose Area Piercing"),
        (ORAL_AREA_PIERCING, "Oral Area Piercing"),
        (SURFACE_PIERCING, "Surface Piercing"),
        (VAGINAL_AREA_PIERCING, "Vaginal Area Piercing"),
    ]

    category = models.CharField(
        max_length=30,
        choices=PIERCING_CATEGORIES,
        unique=True,
    )

    def __str__(self):
        return self.category

class BellyPiercing(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    Belly=models.BooleanField(default=False)

    def __str__(self):
        return "belly"

class EarAreaPiercing(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    Regular_earlobe = models.BooleanField(default=False)
    Upper_earlobe = models.BooleanField(default=False)
    Helix = models.BooleanField(default=False)
    Industrial = models.BooleanField(default=False)
    Tragus = models.BooleanField(default=False)
    Rook = models.BooleanField(default=False)
    Conch = models.BooleanField(default=False)
    Daith = models.BooleanField(default=False)
    Snug = models.BooleanField(default=False)
    Forward_helix = models.BooleanField(default=False)
    Anti_helix = models.BooleanField(default=False)
    Anti_tragus = models.BooleanField(default=False)
    Auricle = models.BooleanField(default=False)
    Axternal_auditory_meatus = models.BooleanField(default=False)
    Transverse_lobe = models.BooleanField(default=False)

    def __str__(self):
        return "Ear Area Piercing"


class FacialAreaPiercing(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    Cheek = models.BooleanField(default=False)
    Eyebrow = models.BooleanField(default=False)
    Sideburn = models.BooleanField(default=False)

    def __str__(self):
        return "Facial Area Piercing"

class JewelrySwapPiercing(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    Nose_area = models.BooleanField(default=False)
    Ear_area = models.BooleanField(default=False)
    Belly = models.BooleanField(default=False)
    Oral_area = models.BooleanField(default=False)
    Facial_area = models.BooleanField(default=False)
    Nipple = models.BooleanField(default=False)
    Surface = models.BooleanField(default=False)
    Vaginal_area = models.BooleanField(default=False)

    def __str__(self):
        return "Jewelry Swap Piercing"


class NipplePiercing(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    Nipple = models.BooleanField(default=False)

    def __str__(self):
        return "Nipple Piercing"


class NoseAreaPiercing(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    Nostril = models.BooleanField(default=False)
    Septum = models.BooleanField(default=False)
    Austin_bar = models.BooleanField(default=False)
    Erl = models.BooleanField(default=False)
    High_nostril = models.BooleanField(default=False)
    Nostril_nasallang = models.BooleanField(default=False)
    Rhino = models.BooleanField(default=False)
    Septril = models.BooleanField(default=False)
    Third_eye = models.BooleanField(default=False)

    def __str__(self):
        return "Nose Area Piercing"


class OralAreaPiercing(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    straight_bar_tongue = models.BooleanField(default=False)
    snake_eye_tongue = models.BooleanField(default=False)
    snake_bite_lip = models.BooleanField(default=False)
    tongue_web = models.BooleanField(default=False)
    smiley = models.BooleanField(default=False)
    monroe = models.BooleanField(default=False)
    medusa = models.BooleanField(default=False)
    madonna = models.BooleanField(default=False)
    dimples = models.BooleanField(default=False)
    ashley = models.BooleanField(default=False)
    angel_bites = models.BooleanField(default=False)
    canine_bites = models.BooleanField(default=False)
    cyber_bites = models.BooleanField(default=False)
    dahlia = models.BooleanField(default=False)
    dolphin_bites = models.BooleanField(default=False)
    frowney = models.BooleanField(default=False)
    gum = models.BooleanField(default=False)
    horizontal_lip = models.BooleanField(default=False)
    jestrum = models.BooleanField(default=False)
    multi_tongue = models.BooleanField(default=False)
    shark_bites = models.BooleanField(default=False)
    spider_bites = models.BooleanField(default=False)
    vampire = models.BooleanField(default=False)
    venom = models.BooleanField(default=False)
    vertical_labret = models.BooleanField(default=False)

    def __str__(self):
        return "Oral Area Piercing"


class SurfacePiercing(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    arm = models.BooleanField(default=False)
    back = models.BooleanField(default=False)
    chest = models.BooleanField(default=False)
    face = models.BooleanField(default=False)
    finger = models.BooleanField(default=False)
    foot = models.BooleanField(default=False)
    hand = models.BooleanField(default=False)
    hip = models.BooleanField(default=False)
    leg = models.BooleanField(default=False)
    neck = models.BooleanField(default=False)
    pelvic = models.BooleanField(default=False)
    ribs = models.BooleanField(default=False)
    shoulder = models.BooleanField(default=False)
    stomach = models.BooleanField(default=False)

    def __str__(self):
        return "Surface Piercing"


class VaginalAreaPiercing(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    christina = models.BooleanField(default=False)
    vertical_hood = models.BooleanField(default=False)
    horizontal_hood = models.BooleanField(default=False)
    inner_labia = models.BooleanField(default=False)
    outer_labia = models.BooleanField(default=False)
    fourchette = models.BooleanField(default=False)
    hymen = models.BooleanField(default=False)
    isabella = models.BooleanField(default=False)
    princess_albertina = models.BooleanField(default=False)
    triangle = models.BooleanField(default=False)

    def __str__(self):
        return "Vaginal Area Piercing"
    communicable_disease = models.BooleanField(default=False)

class ToothGems(models.Model):
    body_location=models.ForeignKey(ServiceCategories,on_delete=models.CASCADE)
    Name=models.CharField(max_length=30)
    ToothGems_Image=models.ImageField()

    def __str__(self):
        return self.Name

class TattooRemoval(models.Model):
    #body_location=models.ForeignKey(BodyLocation,on_delete=models.CASCADE)
    Name=models.CharField(max_length= 30)
    Parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    body_location = models.ForeignKey(ServiceCategories, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name

class PermanentMakeUp(models.Model):
    body_location=models.ForeignKey(ServiceCategories, on_delete=models.CASCADE)
    EyeBrows=models.BooleanField(default=False)
    Eyeliner=models.BooleanField(default=False)
    Lips=models.BooleanField(default=False)

    def __str__(self):
        return self.EyeBrows
    
class SMP(models.Model):
    body_location=models.ForeignKey(ServiceCategories, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    description = models.TextField()
    image_file = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Name

class TattooMedicalRecord(models.Model):
    Selected_field = models.ForeignKey(Tattoo, on_delete=models.CASCADE, related_name="medical_records")
    tattoo_before = models.BooleanField(default=False)
    pregnant_nursing = models.BooleanField(default=False)
    hemophilics_med = models.BooleanField(default=False)
    medical_skin_condition = models.BooleanField(default=False)
    influence_alcohol_drugs = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    health_conditions = models.BooleanField(default=False)

class PiercingMedicalRecord(models.Model):
    # Selected_field = models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE, related_name="medical_records")
    service_category = models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    pierced_before = models.BooleanField(default=False)
    pregnant_nursing = models.BooleanField(default=False)
    hemophiliac_meds = models.BooleanField(default=False)
    medical_skin_conditions = models.BooleanField(default=False)
    communicable_diseases = models.BooleanField(default=False)
    influence_alcohol_drugs = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    health_conditions = models.BooleanField(default=False)

class ToothGemMedicalRecord(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tooth_gem_medical_records")

    service_category = models.ForeignKey(ToothGems, on_delete=models.CASCADE)
    influence_alcohol_drugs = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    medical_skin_conditions = models.BooleanField(default=False)
    communicable_diseases = models.BooleanField(default=False)
    health_conditions = models.BooleanField(default=False)
    sensitive_teeth = models.BooleanField(default=False)
    synthetic_teeth = models.BooleanField(default=False)

class TattooRemovalMedicalRecord(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tattoo_removal_medical_records")
    service_category = models.ForeignKey(TattooRemoval, on_delete=models.CASCADE)
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

class PermanentMakeUpMedicalRecord(models.Model):
    Selected_field = models.ForeignKey(PermanentMakeUp, on_delete=models.CASCADE, related_name="medical_records")
    tattoo_before = models.BooleanField(default=False)
    pregnant_nursing = models.BooleanField(default=False)
    hemophilics_med = models.BooleanField(default=False)
    medical_skin_condition = models.BooleanField(default=False)
    communicable_disease = models.BooleanField(default=False)
    influence_alcohol_drugs = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    health_conditions = models.BooleanField(default=False)

class SMPMedicalRecord(models.Model):
    Selected_field = models.ForeignKey(SMP, on_delete=models.CASCADE, related_name="medical_records")
    tattoo_before = models.BooleanField(default=False)
    pregnant_nursing = models.BooleanField(default=False)
    hemophilics_med = models.BooleanField(default=False)
    medical_skin_condition = models.BooleanField(default=False)
    communicable_disease = models.BooleanField(default=False)
    influence_alcohol_drugs = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    health_conditions = models.BooleanField(default=False)

class EmergencyContact(models.Model):
    Selected_services = models.ForeignKey(ServiceCategories, on_delete=models.CASCADE, related_name="emergency_contacts")
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=16)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class DoctorInfo(models.Model):
    Emergency_Contact = models.ForeignKey(EmergencyContact, on_delete=models.CASCADE, related_name="doctor_info")
    Doctor_name = models.CharField(max_length=30)
    Docotr_phone = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class TattoWaiver(models.Model):
    body_location=models.ForeignKey(Tattoo, on_delete=models.CASCADE, default=None)
    client_name = models.CharField(max_length=255)
    age_initials = models.BooleanField(default=False)
    mental_medical_initials = models.BooleanField(default=False)
    care_instructions_initials = models.BooleanField(default=False)
    colors_variability_initials = models.BooleanField(default=False)
    release_of_liability_initials = models.BooleanField(default=False)
    hold_harmless_initials = models.BooleanField(default=False)
    damages_and_injuries_initials = models.BooleanField(default=False)
    permanent_change_initials = models.BooleanField(default=False)
    tattoo_removal_caution_initials = models.BooleanField(default=False)
    consent_for_photographs_initials = models.BooleanField(default=False)
    infection_information_initials = models.BooleanField(default=False)
    consent_for_communication_initials = models.BooleanField(default=False)
    information_is_true_initials = models.BooleanField(default=False)
    signature_file = models.FileField(upload_to='signatures/')
    timestamp = models.DateTimeField(auto_now_add=True)

class PiercingWaiver(models.Model):
    body_location=models.ForeignKey(BodyLocationPiercing, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    age_initials = models.BooleanField(default=False)
    mental_medical_initials = models.BooleanField(default=False)
    care_instructions_initials = models.BooleanField(default=False)
    colors_variability_initials = models.BooleanField(default=False)
    release_of_liability_initials = models.BooleanField(default=False)
    hold_harmless_initials = models.BooleanField(default=False)
    damages_and_injuries_initials = models.BooleanField(default=False)
    permanent_change_initials = models.BooleanField(default=False)
    tattoo_removal_caution_initials = models.BooleanField(default=False)
    consent_for_photographs_initials = models.BooleanField(default=False)
    infection_information_initials = models.BooleanField(default=False)
    consent_for_communication_initials = models.BooleanField(default=False)
    information_is_true_initials = models.BooleanField(default=False)
    signature_file = models.FileField(upload_to='signatures/')
    timestamp = models.DateTimeField(auto_now_add=True)

class ToothGemsWaiver(models.Model):
    body_location=models.ForeignKey(ToothGems, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    age_initials = models.BooleanField(default=False)
    mental_medical_initials = models.BooleanField(default=False)
    care_instructions_initials = models.BooleanField(default=False)
    colors_variability_initials = models.BooleanField(default=False)
    release_of_liability_initials = models.BooleanField(default=False)
    hold_harmless_initials = models.BooleanField(default=False)
    damages_and_injuries_initials = models.BooleanField(default=False)
    permanent_change_initials = models.BooleanField(default=False)
    tattoo_removal_caution_initials = models.BooleanField(default=False)
    consent_for_photographs_initials = models.BooleanField(default=False)
    infection_information_initials = models.BooleanField(default=False)
    consent_for_communication_initials = models.BooleanField(default=False)
    information_is_true_initials = models.BooleanField(default=False)
    signature_file = models.FileField(upload_to='signatures/')
    timestamp = models.DateTimeField(auto_now_add=True)

class TattoremovalWaiver(models.Model):
    body_location=models.ForeignKey(TattooRemoval, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    age_initials = models.BooleanField(default=False)
    mental_medical_initials = models.BooleanField(default=False)
    care_instructions_initials = models.BooleanField(default=False)
    colors_variability_initials = models.BooleanField(default=False)
    release_of_liability_initials = models.BooleanField(default=False)
    hold_harmless_initials = models.BooleanField(default=False)
    damages_and_injuries_initials = models.BooleanField(default=False)
    permanent_change_initials = models.BooleanField(default=False)
    tattoo_removal_caution_initials = models.BooleanField(default=False)
    consent_for_photographs_initials = models.BooleanField(default=False)
    infection_information_initials = models.BooleanField(default=False)
    consent_for_communication_initials = models.BooleanField(default=False)
    information_is_true_initials = models.BooleanField(default=False)
    signature_file = models.FileField(upload_to='signatures/')
    timestamp = models.DateTimeField(auto_now_add=True)


class PermanentMakeUpWaiver(models.Model):
    body_location=models.ForeignKey(PermanentMakeUp, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    age_initials = models.BooleanField(default=False)
    mental_medical_initials = models.BooleanField(default=False)
    care_instructions_initials = models.BooleanField(default=False)
    colors_variability_initials = models.BooleanField(default=False)
    release_of_liability_initials = models.BooleanField(default=False)
    hold_harmless_initials = models.BooleanField(default=False)
    damages_and_injuries_initials = models.BooleanField(default=False)
    permanent_change_initials = models.BooleanField(default=False)
    tattoo_removal_caution_initials = models.BooleanField(default=False)
    consent_for_photographs_initials = models.BooleanField(default=False)
    infection_information_initials = models.BooleanField(default=False)
    consent_for_communication_initials = models.BooleanField(default=False)
    information_is_true_initials = models.BooleanField(default=False)
    signature_file = models.FileField(upload_to='signatures/')
    timestamp = models.DateTimeField(auto_now_add=True)


class SMPWaiver(models.Model):
    body_location=models.ForeignKey(SMP, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    age_initials = models.BooleanField(default=False)
    mental_medical_initials = models.BooleanField(default=False)
    care_instructions_initials = models.BooleanField(default=False)
    colors_variability_initials = models.BooleanField(default=False)
    release_of_liability_initials = models.BooleanField(default=False)
    hold_harmless_initials = models.BooleanField(default=False)
    damages_and_injuries_initials = models.BooleanField(default=False)
    permanent_change_initials = models.BooleanField(default=False)
    tattoo_removal_caution_initials = models.BooleanField(default=False)
    consent_for_photographs_initials = models.BooleanField(default=False)
    infection_information_initials = models.BooleanField(default=False)
    consent_for_communication_initials = models.BooleanField(default=False)
    information_is_true_initials = models.BooleanField(default=False)
    signature_file = models.FileField(upload_to='signatures/')
    timestamp = models.DateTimeField(auto_now_add=True)

class WaiverAgreement(models.Model):
    body_location=models.ForeignKey(ServiceCategories, on_delete= models.CASCADE, default=None)
    name = models.CharField(max_length=255, verbose_name="Name")
    agreement_text = models.TextField(
        verbose_name="Agreement Text",
        help_text="Copy and paste the entire agreement text here.",
    )
    initials = models.BooleanField(default=False, verbose_name="Initials")
    signature = models.ImageField(
        upload_to="waiver_signatures/",
        verbose_name="Signature",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Waiver Agreement"
        verbose_name_plural = "Waiver Agreements"


class TermsOfService(models.Model):
    service_category = models.ForeignKey(ServiceCategories, on_delete=models.CASCADE)