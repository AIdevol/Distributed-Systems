from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', views.userviewsets)
router.register(r'Parent-details', views.Parentaldetailsviewsets)
router.register(r'userdetails', views.userdetailsviewsets)
router.register(r'ServiceCategory', views.ServiceCategoryviewsets)
router.register(r'User_selected_category',views.User_selected_category_viewsets)
router.register(r'Shared-Medica-lRecord', views.SharedMedicalRecordviewsets)
router.register(r'Emergency_Contact', views.Emergency_Contact_viewsets)
router.register(r'DoctorInfo',views.DoctorInfoviewsets)
router.register(r'Shared-Waiver-And-Release', views.SharedWaiverAndReleaseviewsets)
router.register(r'Hold-Harmless-Release-Agreement',views.HoldHarmlessAgreementviewsets)
router.register(r'piercing-medical-records', views.PiercingMedicalRecordViewSet)
router.register(r'tooth-gem-medical-records', views.ToothGemMedicalRecordViewSet)
router.register(r'tattoo-removal-medical-records', views.TattooRemovalMedicalRecordViewSet)
router.register(r'piercing-waiver-and-r eleases', views.PiercingWaiverAndReleaseViewSet)
router.register(r'tooth-gem-waiver-and-releases', views.ToothGemWaiverAndReleaseViewSet)
router.register(r'tattoo-removal-waiver-and-releases', views.TattooRemovalWaiverAndReleaseViewSet)
router.register(r'terms-and-conditions',views.TermAndConditionsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
