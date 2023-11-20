from rest_framework import viewsets
from .models import (SMP, Ankle, Arm, Back, BellyPiercing, BodyLocationPiercing, DoctorInfo, Ear, EarAreaPiercing, EmergencyContact, FacialAreaPiercing, Foot, Glutes, Hand, Hip, JewelrySwapPiercing, Knee, Leg, LowerLeg, NipplePiercing, OralAreaPiercing, Pelvic, PermanentMakeUp, PermanentMakeUpMedicalRecord, PermanentMakeUpWaiver, PiercingMedicalRecord, PiercingWaiver, SMPMedicalRecord, SMPWaiver, Scalp, ServiceCategories, SurfacePiercing, TattoWaiver, Tattoo, TattooMedicalRecord, TattooRemoval, TattooRemovalMedicalRecord, TattoremovalWaiver, TermsOfService, Thigh, ToothGemMedicalRecord, ToothGems, ToothGemsWaiver, Torso, UserService, BodyLocation, Head, Neck, Nipple, Under_chest, Face,
                    Forehead,Temple, Eye_Brow, Eyelid, Nose, Cheeks, Lip, Jaw, VaginalAreaPiercing, WaiverAgreement)
from .serializers import (
    AnkleSerializer, ArmSerializer, BackSerializer, BellyPiercingSerializer, BodyLocationPiercingSerializer, EarAreaPiercingSerilizer, EarSerializer,
    FacialAreaPiercingSerializer, FootSerializer, GlutesSerializer, HandSerializer, HipSerializer, 
    JewelrySwapPiercingSerializer, KneeSerializer, LegSerializer, LowerLegSerializer, NipplePiercingSerializer, OralAreaPiercingSerializer,
    PelvicSerializer, PermanentMakeUpSerializer, PiercingWaiverSerializer, SMPSerializer, SMPWaiverSerializer, ScalpSerializer, ServiceCategoriesSerializer, SurfacePiercingSerializer, TattoWaiverSerializer, 
    TattooRemovalSerializer, TattooRemovalWaiverSerializer, TattooSerializer, TermsOfConditionsSerializer, ThighSerializer, ToothGemsSerializer, TootheGemsSerializer, TorsoSerializer, UserServiceSerializer, BodyLocationSerializer,
    HeadSerializer, NeckSerializer, NippleSerializer, UnderChestSerializer,
    FaceSerializer, ForeheadSerializer,TempleSerializer, Eye_BrowSerializer, EyelidSerializer,
    NoseSerializer, CheeksSerializer, LipSerializer, JawSerializer, VaginalAreaPiercingSerializer,TattooMedicalRecordSerializer,
    PiercingMedicalRecordSerializer, ToothGemMedicalRecordSerializer, TattooRemovalMedicalRecordSerializer, PermanentMakeUpMedicalRecordSerializer, 
    SMPMedicalRecordSerializer, EmergencyContactSerializer, DoctorInfoSerializer, WaiverAgreementSerializer

)

class ServiceCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategories.objects.all()
    serializer_class = ServiceCategoriesSerializer

class UserServiceViewSet(viewsets.ModelViewSet):
    queryset = UserService.objects.all()
    serializer_class = UserServiceSerializer

class BodyLocationViewSet(viewsets.ModelViewSet):
    queryset = BodyLocation.objects.all()
    serializer_class = BodyLocationSerializer

class HeadViewSet(viewsets.ModelViewSet):
    queryset = Head.objects.all()
    serializer_class = HeadSerializer

class NeckViewSet(viewsets.ModelViewSet):
    queryset = Neck.objects.all()
    serializer_class = NeckSerializer

class NippleViewSet(viewsets.ModelViewSet):
    queryset = Nipple.objects.all()
    serializer_class = NippleSerializer

class UnderChestViewSet(viewsets.ModelViewSet):
    queryset = Under_chest.objects.all()
    serializer_class = UnderChestSerializer

class FaceViewSet(viewsets.ModelViewSet):
    queryset = Face.objects.all()
    serializer_class = FaceSerializer

class ForeheadViewSet(viewsets.ModelViewSet):
    queryset = Forehead.objects.all()
    serializer_class = ForeheadSerializer

class TempleViewSet(viewsets.ModelViewSet):
    queryset = Temple.objects.all()
    serializer_class = TempleSerializer

class Eye_BrowViewSet(viewsets.ModelViewSet):
    queryset = Eye_Brow.objects.all()
    serializer_class = Eye_BrowSerializer

class EyelidViewSet(viewsets.ModelViewSet):
    queryset = Eyelid.objects.all()
    serializer_class = EyelidSerializer

class NoseViewSet(viewsets.ModelViewSet):
    queryset = Nose.objects.all()
    serializer_class = NoseSerializer

class CheeksViewSet(viewsets.ModelViewSet):
    queryset = Cheeks.objects.all()
    serializer_class = CheeksSerializer

class LipViewSet(viewsets.ModelViewSet):
    queryset = Lip.objects.all()
    serializer_class = LipSerializer

class JawViewSet(viewsets.ModelViewSet):
    queryset = Jaw.objects.all()
    serializer_class = JawSerializer

class TattooViewSet(viewsets.ModelViewSet):
    queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer

class ScalpViewset(viewsets.ModelViewSet):
    queryset=Scalp.objects.all()
    serializer_class=ScalpSerializer

class EarViewsets(viewsets.ModelViewSet):
    queryset = Ear.objects.all()
    serializer_class=EarSerializer

class TorsoViewsets(viewsets.ModelViewSet):
    queryset = Torso.objects.all()
    serializer_class=TorsoSerializer

class BackViewsets(viewsets.ModelViewSet):
    queryset = Back.objects.all()
    serializer_class=BackSerializer

class ArmViewSet(viewsets.ModelViewSet):
    queryset = Arm.objects.all()
    serializer_class = ArmSerializer

class HandViewSet(viewsets.ModelViewSet):
    queryset = Hand.objects.all()
    serializer_class = HandSerializer

class HipViewSet(viewsets.ModelViewSet):
    queryset = Hip.objects.all()
    serializer_class = HipSerializer

class GlutesViewSet(viewsets.ModelViewSet):
    queryset = Glutes.objects.all()
    serializer_class = GlutesSerializer

class PelvicViewSet(viewsets.ModelViewSet):
    queryset = Pelvic.objects.all()
    serializer_class = PelvicSerializer

class LegViewSet(viewsets.ModelViewSet):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer

class LegViewSet(viewsets.ModelViewSet):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer

class LegViewSet(viewsets.ModelViewSet):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer

class ThighViewSet(viewsets.ModelViewSet):
    queryset = Thigh.objects.all()
    serializer_class = ThighSerializer

class KneeViewSet(viewsets.ModelViewSet):
    queryset = Knee.objects.all()
    serializer_class = KneeSerializer

class LowerLegViewSet(viewsets.ModelViewSet):
    queryset = LowerLeg.objects.all()
    serializer_class = LowerLegSerializer

class AnkleViewSet(viewsets.ModelViewSet):
    queryset = Ankle.objects.all()
    serializer_class = AnkleSerializer

class FootViewSet(viewsets.ModelViewSet):
    queryset = Foot.objects.all()
    serializer_class=FootSerializer

#piercing views

class BodyLocationPiercingViewSet(viewsets.ModelViewSet):
    queryset = BodyLocationPiercing.objects.all()
    serializer_class = BodyLocationPiercingSerializer

class BellyPiercingViewSet(viewsets.ModelViewSet):
    queryset = BellyPiercing.objects.all()
    serializer_class = BellyPiercingSerializer


class EarAreaPiercingViewSet(viewsets.ModelViewSet):
    queryset = EarAreaPiercing.objects.all()
    serializer_class = EarAreaPiercingSerilizer


class FacialAreaPiercingViewSet(viewsets.ModelViewSet):
    queryset = FacialAreaPiercing.objects.all()
    serializer_class = FacialAreaPiercingSerializer


class JewelrySwapPiercingViewSet(viewsets.ModelViewSet):
    queryset = JewelrySwapPiercing.objects.all()
    serializer_class = JewelrySwapPiercingSerializer


class NipplePiercingViewSet(viewsets.ModelViewSet):
    queryset = NipplePiercing.objects.all()
    serializer_class = NipplePiercingSerializer


class OralAreaPiercingViewSet(viewsets.ModelViewSet):
    queryset = OralAreaPiercing.objects.all()
    serializer_class = OralAreaPiercingSerializer


class SurfacePiercingViewSet(viewsets.ModelViewSet):
    queryset = SurfacePiercing.objects.all()
    serializer_class = SurfacePiercingSerializer


class VaginalAreaPiercingViewSet(viewsets.ModelViewSet):
    queryset = VaginalAreaPiercing.objects.all()
    serializer_class = VaginalAreaPiercingSerializer

class ToothgemsViewSet(viewsets.ModelViewSet):
    queryset=ToothGems.objects.all()
    serializer_class = TootheGemsSerializer
class TattooRemovalViewSet(viewsets.ModelViewSet):
    queryset = TattooRemoval.objects.all()
    serializer_class = TattooRemovalSerializer

class PermanentMakeUpViewSet(viewsets.ModelViewSet):
    queryset = PermanentMakeUp.objects.all()
    serializer_class = PermanentMakeUpSerializer

class SMPViewSet(viewsets.ModelViewSet):
    queryset = SMP.objects.all()
    serializer_class = SMPSerializer


class TattooMedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = TattooMedicalRecordSerializer
    queryset = TattooMedicalRecord.objects.all()


class PiercingMedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = PiercingMedicalRecordSerializer
    queryset = PiercingMedicalRecord.objects.all()


class ToothGemMedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = ToothGemMedicalRecordSerializer
    queryset = ToothGemMedicalRecord.objects.all()


class TattooRemovalMedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = TattooRemovalMedicalRecordSerializer
    queryset = TattooRemovalMedicalRecord.objects.all()


class PermanentMakeUpMedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = PermanentMakeUpMedicalRecordSerializer
    queryset = PermanentMakeUpMedicalRecord.objects.all()


class SMPMedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = SMPMedicalRecordSerializer
    queryset = SMPMedicalRecord.objects.all()


class EmergencyContactViewSet(viewsets.ModelViewSet):
    serializer_class = EmergencyContactSerializer
    queryset = EmergencyContact.objects.all()


class DoctorInfoViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorInfoSerializer
    queryset = DoctorInfo.objects.all()

class TattoWaiverViewSet(viewsets.ModelViewSet):
    queryset = TattoWaiver.objects.all()
    serializer_class = TattoWaiverSerializer

class PiercingWaiverViewset(viewsets.ModelViewSet):
    queryset = PiercingWaiver.objects.all()
    serializer_class = PiercingWaiverSerializer

class ToothGemsViewSet(viewsets.ModelViewSet):
    queryset = ToothGemsWaiver.objects.all()
    serializer_class = ToothGemsSerializer

class TattooRemovalViewSet(viewsets.ModelViewSet):
    queryset = TattoremovalWaiver.objects.all()
    serializer_class = TattooRemovalWaiverSerializer

class PermanentMakeUpViewSet(viewsets.ModelViewSet):
    queryset = PermanentMakeUpWaiver.objects.all()
    serializer_class = PermanentMakeUpSerializer

class SMPWaiverViewSet(viewsets.ModelViewSet):
    queryset = SMPWaiver.objects.all()
    serializer_class = SMPWaiverSerializer

class WaiverAgreementViewSet(viewsets.ModelViewSet):
    queryset=WaiverAgreement.objects.all()
    serializer_class=WaiverAgreementSerializer

class TermsOfServiceViewSet(viewsets.ModelViewSet):
    queryset=TermsOfService.objects.all()
    serializer_class=TermsOfConditionsSerializer
