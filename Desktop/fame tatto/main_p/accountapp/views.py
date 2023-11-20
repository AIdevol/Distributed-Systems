from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    userdetails,
    user,
    ParentDetails,
    ServiceCategory,
    User_selected_category,
    SharedMedicalRecord,
    Emergency_Contact,
    DoctorInfo,
    SharedWaiverAndRelease,
    HoldHarmlessAgreement,
    PiercingMedicalRecord,
    ToothGemWaiverAndRelease,
    TattooRemovalMedicalRecord,
    ToothGemMedicalRecord,
    PiercingWaiverAndRelease,
    TattooRemovalWaiverAndRelease,
    TermAndConditions,

)
from .serializers import (
    userserializers,
    ParentDetailsSerializers,
    userdetailsserializers,
    userserializers,
    ServiceCategoryserializers,
    User_selected_category_serializers,
    SharedMedicalRecordSerializers,
    Emergency_Contact_Serializers,
    DoctorInfoSerializers,
    SharedWaiverAndReleaseserializers,
    HoldHarmlessAgreementserializers,
    PiercingMedicalRecordSerializers,
    ToothGemWaiverAndReleaseSerializers,
    TattooRemovalMedicalRecordSerializers,
    ToothGemMedicalRecordSerializers,
    PiercingWaiverAndReleaseSerializers,
    TattooRemovalWaiverAndReleaseSerializers,
    TermAndConditionsSerializers,
)  

class userviewsets(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userserializers

class Parentaldetailsviewsets(viewsets.ModelViewSet):
    queryset = ParentDetails.objects.all()
    serializer_class = ParentDetailsSerializers

class userdetailsviewsets(viewsets.ModelViewSet):
    queryset=userdetails.objects.all()
    serializer_class = userdetailsserializers

class ServiceCategoryviewsets(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategoryserializers

class User_selected_category_viewsets(viewsets.ModelViewSet):
    queryset=User_selected_category.objects.all()
    serializer_class=User_selected_category_serializers

class SharedMedicalRecordviewsets(viewsets. ModelViewSet):
    queryset=SharedMedicalRecord.objects.all()
    serializer_class= SharedMedicalRecordSerializers

class Emergency_Contact_viewsets(viewsets.ModelViewSet):
    queryset=Emergency_Contact.objects.all()
    serializer_class=Emergency_Contact_Serializers

class DoctorInfoviewsets(viewsets.ModelViewSet):
    queryset=DoctorInfo.objects.all()
    serializer_class=DoctorInfoSerializers

class SharedWaiverAndReleaseviewsets(viewsets.ModelViewSet):
    queryset=SharedWaiverAndRelease.objects.all()
    serializer_class=SharedWaiverAndReleaseserializers

class HoldHarmlessAgreementviewsets(viewsets.ModelViewSet):
    queryset=HoldHarmlessAgreement.objects.all()
    serializer_class=HoldHarmlessAgreementserializers

class SharedMedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = SharedMedicalRecord.objects.all()
    serializer_class = SharedMedicalRecordSerializers

class SharedWaiverAndReleaseViewSet(viewsets.ModelViewSet):
    queryset = SharedWaiverAndRelease.objects.all()
    serializer_class = SharedWaiverAndReleaseserializers

class PiercingMedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = PiercingMedicalRecord.objects.all()
    serializer_class = PiercingMedicalRecordSerializers

class ToothGemMedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = ToothGemMedicalRecord.objects.all()
    serializer_class = ToothGemMedicalRecordSerializers

class TattooRemovalMedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = TattooRemovalMedicalRecord.objects.all()
    serializer_class = TattooRemovalMedicalRecordSerializers

class PiercingWaiverAndReleaseViewSet(viewsets.ModelViewSet):
    queryset = PiercingWaiverAndRelease.objects.all()
    serializer_class = PiercingWaiverAndReleaseSerializers

class ToothGemWaiverAndReleaseViewSet(viewsets.ModelViewSet):
    queryset = ToothGemWaiverAndRelease.objects.all()
    serializer_class = ToothGemWaiverAndReleaseSerializers

class TattooRemovalWaiverAndReleaseViewSet(viewsets.ModelViewSet):
    queryset = TattooRemovalWaiverAndRelease.objects.all()
    serializer_class = TattooRemovalWaiverAndReleaseSerializers


class TermAndConditionsViewSet(viewsets.ModelViewSet):
    queryset = TermAndConditions.objects.all()
    serializer_class = TermAndConditionsSerializers
