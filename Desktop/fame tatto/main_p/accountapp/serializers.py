from .models import (
    ServiceCategory,
    user,
    ParentDetails,
    userdetails, 
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
from rest_framework import serializers

class userserializers(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"

class ParentDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParentDetails
        fields= "__all__"

class userdetailsserializers(serializers.ModelSerializer):
    class Meta:
        model = userdetails
        fields = "__all__"

class ServiceCategoryserializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"

class User_selected_category_serializers(serializers.ModelSerializer):
    class Meta:
        model=User_selected_category
        fields="__all__"


class SharedMedicalRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model= SharedMedicalRecord
        fields ="__all__"

class Emergency_Contact_Serializers(serializers.ModelSerializer):
    class Meta:
        model= Emergency_Contact
        fields = "__all__"

class DoctorInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model= DoctorInfo
        fields = "__all__"

class SharedWaiverAndReleaseserializers(serializers.ModelSerializer):
    class Meta:
        model=SharedWaiverAndRelease
        fields="__all__"

class HoldHarmlessAgreementserializers(serializers.ModelSerializer):
    class Meta:
        models= HoldHarmlessAgreement
        fields="__all__"

class SharedMedicalRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = SharedMedicalRecord
        fields = '__all__'

class SharedWaiverAndReleaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = SharedWaiverAndRelease
        fields = '__all__'

class PiercingMedicalRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = PiercingMedicalRecord
        fields = '__all__'

class ToothGemMedicalRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToothGemMedicalRecord
        fields = '__all__'

class TattooRemovalMedicalRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = TattooRemovalMedicalRecord
        fields = '__all__'

class PiercingWaiverAndReleaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = PiercingWaiverAndRelease
        fields = '__all__'

class ToothGemWaiverAndReleaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToothGemWaiverAndRelease
        fields = '__all__'

class TattooRemovalWaiverAndReleaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = TattooRemovalWaiverAndRelease
        fields = '__all__'

class TermAndConditionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TermAndConditions
        fields = '__all__'
