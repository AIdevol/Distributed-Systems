from rest_framework import serializers
from .models import (
    SMP, Ankle, Arm, Back, BellyPiercing, BodyLocationPiercing, Ear, EarAreaPiercing, FacialAreaPiercing, Foot, Glutes, Hand, Hip, JewelrySwapPiercing, Knee, Leg, LowerLeg, NipplePiercing, OralAreaPiercing, Pelvic, PermanentMakeUp, PermanentMakeUpWaiver, PiercingWaiver, SMPWaiver, Scalp, ServiceCategories, SurfacePiercing, TattoWaiver, Tattoo, TattooRemoval, TattoremovalWaiver, TermsOfService, Thigh, ToothGems, ToothGemsWaiver,
    Torso, UserService, BodyLocation, Head, Neck, Nipple, Under_chest, 
    Face, Forehead,Temple, Eye_Brow, Eyelid, Nose, Cheeks, Lip, Jaw, VaginalAreaPiercing,TattooMedicalRecord, PiercingMedicalRecord, ToothGemMedicalRecord,
    TattooRemovalMedicalRecord, PermanentMakeUpMedicalRecord, SMPMedicalRecord, EmergencyContact, DoctorInfo, WaiverAgreement
 )


class ServiceCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategories
        fields = '__all__'

class UserServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserService
        fields = '__all__'

class BodyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyLocation
        fields = '__all__'

class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head
        fields = '__all__'

class NeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neck
        fields = '__all__'

class NippleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nipple
        fields = '__all__'

class UnderChestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Under_chest
        fields = '__all__'

class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = '__all__'

class ForeheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forehead
        fields = '__all__'

class TattooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattoo
        fields = '__all__'

class TempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temple
        fields = '__all__'

class Eye_BrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eye_Brow
        fields = '__all__'

class EyelidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eyelid
        fields = '__all__'

class NoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nose
        fields = '__all__'

class CheeksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheeks
        fields = '__all__'

class LipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lip
        fields = '__all__'

class JawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jaw
        fields = '__all__'

class ScalpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scalp
        fields='__all__'

class EarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ear
        fields= '__all__'

class TorsoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torso
        fields= "__all__"

class BackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Back
        fields='__all__'

class ArmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arm
        fields = '__all__'

class HandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hand
        fields = '__all__'

class HipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hip
        fields = '__all__'

class GlutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glutes
        fields = '__all__'

class PelvicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelvic
        fields = '__all__'

class LegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leg
        fields = '__all__'

class ThighSerializer(serializers.ModelSerializer):
    class Meta:
        model= Thigh
        fields='__all__'

class KneeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Knee
        fields='__all__'

class LowerLegSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowerLeg
        fields = '__all__'

class AnkleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ankle
        fields = '__all__'

class FootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foot
        fields = '__all__'

#piercing serializers

class BodyLocationPiercingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyLocationPiercing
        fields = '__all__'

class BellyPiercingSerializer(serializers.ModelSerializer):
    class Meta:
        model=BellyPiercing
        fields='__all__'

class EarAreaPiercingSerilizer(serializers.ModelSerializer):
    class Meta:
        model=EarAreaPiercing
        fields='__all__'
    
class FacialAreaPiercingSerializer(serializers.ModelSerializer):
    class Meta:
        model=FacialAreaPiercing
        fields='__all__'

class JewelrySwapPiercingSerializer(serializers.ModelSerializer):
    class Meta:
        model=JewelrySwapPiercing
        fields='__all__'

class NipplePiercingSerializer(serializers.ModelSerializer):
    class Meta:
        model=NipplePiercing
        fields='__all__'

class OralAreaPiercingSerializer(serializers.ModelSerializer):
    class Meta:
        model=OralAreaPiercing
        fields='__all__'

class SurfacePiercingSerializer(serializers.ModelSerializer):
    class Meta:
        model=SurfacePiercing
        fields='__all__'

class VaginalAreaPiercingSerializer(serializers.ModelSerializer):
    class Meta:
        model=VaginalAreaPiercing
        fields="__all__"

class TootheGemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToothGems
        fields= "__all__"

class TattooRemovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooRemoval
        fields = '__all__'

class PermanentMakeUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentMakeUp
        fields = '__all__'

class SMPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMP
        fields = '__all__'

class TattooMedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooMedicalRecord
        fields = '__all__'


class PiercingMedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiercingMedicalRecord
        fields = '__all__'


class ToothGemMedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToothGemMedicalRecord
        fields = '__all__'


class TattooRemovalMedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooRemovalMedicalRecord
        fields = '__all__'


class PermanentMakeUpMedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentMakeUpMedicalRecord
        fields = '__all__'


class SMPMedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMPMedicalRecord
        fields = '__all__'


class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = '__all__'


class DoctorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInfo
        fields = '__all__'

class TattoWaiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattoWaiver
        fields = '__all__'

class PiercingWaiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiercingWaiver
        fields = '__all__'

class ToothGemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToothGemsWaiver
        fields = '__all__'

class TattooRemovalWaiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattoremovalWaiver
        fields = '__all__'

class PermanentMakeUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentMakeUpWaiver
        fields = '__all__'

class SMPWaiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMPWaiver
        fields = '__all__'

class WaiverAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model=WaiverAgreement
        fields='__all__'

class TermsOfConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TermsOfService
        fields='__all__'