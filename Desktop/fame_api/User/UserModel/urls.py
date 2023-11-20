from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AnkleViewSet, ArmViewSet, BackViewsets, BellyPiercingViewSet, BodyLocationPiercingViewSet, CheeksViewSet, 
    DoctorInfoViewSet, EarAreaPiercingViewSet, EarViewsets, EmergencyContactViewSet, Eye_BrowViewSet, EyelidViewSet, 
    FacialAreaPiercingViewSet, FootViewSet, GlutesViewSet, HandViewSet,
    HipViewSet, JawViewSet, JewelrySwapPiercingViewSet, KneeViewSet, LegViewSet, LipViewSet, LowerLegViewSet, NipplePiercingViewSet, 
    NoseViewSet, OralAreaPiercingViewSet, PelvicViewSet, PermanentMakeUpMedicalRecordViewSet, PermanentMakeUpViewSet, 
    PiercingMedicalRecordViewSet, PiercingWaiverViewset, SMPMedicalRecordViewSet, SMPViewSet, SMPWaiverViewSet, ScalpViewset,
    ServiceCategoriesViewSet, SurfacePiercingViewSet, TattoWaiverViewSet, TattooMedicalRecordViewSet, TattooRemovalMedicalRecordViewSet, 
    TattooRemovalViewSet, TattooViewSet, TempleViewSet, TermsOfServiceViewSet, ThighViewSet, ToothGemMedicalRecordViewSet, ToothGemsViewSet, ToothgemsViewSet, TorsoViewsets, 
    UserServiceViewSet, BodyLocationViewSet,
    HeadViewSet, NeckViewSet, NippleViewSet, UnderChestViewSet,
    FaceViewSet, ForeheadViewSet, VaginalAreaPiercingViewSet, WaiverAgreementViewSet,
)

router = DefaultRouter()
router.register(r'servicecategories', ServiceCategoriesViewSet)
router.register(r'userservice', UserServiceViewSet)
router.register(r'tatto-selection',TattooViewSet)
router.register(r'bodylocation', BodyLocationViewSet)
router.register(r'head', HeadViewSet)
router.register(r'neck', NeckViewSet)
router.register(r'nipple', NippleViewSet)
router.register(r'underchest', UnderChestViewSet)
router.register(r'face', FaceViewSet)
router.register(r'forehead', ForeheadViewSet)
# router.register(r'tattoo', TattooViewSet)
router.register(r'temples', TempleViewSet)
router.register(r'eye_brows', Eye_BrowViewSet)
router.register(r'eyelids', EyelidViewSet)
router.register(r'noses', NoseViewSet)
router.register(r'cheeks', CheeksViewSet)
router.register(r'lips', LipViewSet)
router.register(r'jaws', JawViewSet)
router.register(r'scalp', ScalpViewset)
router.register(r'ear', EarViewsets)
router.register(r'torso', TorsoViewsets)
router.register(r'BackWard', BackViewsets)
router.register(r'Arm', ArmViewSet)
router.register(r'Hand', HandViewSet)
router.register(r'hips', HipViewSet)
router.register(r'glutes', GlutesViewSet)
router.register(r'pelvics', PelvicViewSet)
router.register(r'legs', LegViewSet)
router.register(r'thighs', ThighViewSet)
router.register(r'knees', KneeViewSet)
router.register(r'lowerlegs', LowerLegViewSet)
router.register(r'ankles', AnkleViewSet)
router.register(r'Foot', FootViewSet)
###piercing urls
router.register(r'bodylocationpiercings', BodyLocationPiercingViewSet)
router.register(r'body-location-piercings', BodyLocationPiercingViewSet)
router.register(r'belly-piercings', BellyPiercingViewSet)
router.register(r'ear-area-piercings', EarAreaPiercingViewSet)
router.register(r'facial-area-piercings', FacialAreaPiercingViewSet)
router.register(r'jewelry-swap-piercings', JewelrySwapPiercingViewSet)
router.register(r'nipple-piercings', NipplePiercingViewSet)
router.register(r'oral-area-piercings', OralAreaPiercingViewSet)
router.register(r'surface-piercings', SurfacePiercingViewSet)
router.register(r'vaginal-area-piercings', VaginalAreaPiercingViewSet)
router.register(r'Toothegems', ToothgemsViewSet)
router.register(r'tattooremoval', TattooRemovalViewSet)
router.register(r'permanentmakeup', PermanentMakeUpViewSet)
router.register(r'smp', SMPViewSet)
router.register(r'tattoo_medical_records', TattooMedicalRecordViewSet)
router.register(r'piercing_medical_records', PiercingMedicalRecordViewSet)
router.register(r'tooth_gem_medical_records', ToothGemMedicalRecordViewSet)
router.register(r'tattoo_removal_medical_records', TattooRemovalMedicalRecordViewSet)
router.register(r'permanent_make_up_medical_records', PermanentMakeUpMedicalRecordViewSet)
router.register(r'smp_medical_records', SMPMedicalRecordViewSet)
router.register(r'emergency_contacts', EmergencyContactViewSet)
router.register(r'doctor_info', DoctorInfoViewSet)
router.register(r'Tattoorelease-waiver',TattoWaiverViewSet)
router.register(r'Piercing-Waiver', PiercingWaiverViewset)
router.register(r'tooth-gems-waiver', ToothGemsViewSet)
router.register(r'tattoo-removal-waiver', TattooRemovalViewSet)
router.register(r'permanent-makeupWaiver', PermanentMakeUpViewSet)
router.register(r'smp-waiver', SMPWaiverViewSet)
router.register(r'waiverAgreement', WaiverAgreementViewSet)
router.register(r'TermsOfService', TermsOfServiceViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
