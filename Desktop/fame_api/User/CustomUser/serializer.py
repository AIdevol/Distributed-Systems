from rest_framework import serializers
from .models import CustomUser, GuardianDetails

class GuardianDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardianDetails
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    guardian_details = GuardianDetailsSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        guardian_details_data = validated_data.pop('guardian_details', None)
        user = CustomUser.objects.create_user(**validated_data)

        if guardian_details_data:
            GuardianDetails.objects.create(user=user, **guardian_details_data)

        return user

    def update(self, instance, validated_data):
        guardian_details_data = validated_data.pop('guardian_details', None)

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        instance.save()

        if guardian_details_data:
            guardian_details = instance.guardian_details
            if guardian_details:
                guardian_details.guardian_name = guardian_details_data.get('guardian_name', guardian_details.guardian_name)
                guardian_details.guardian_phone = guardian_details_data.get('guardian_phone', guardian_details.guardian_phone)
                guardian_details.save()
            else:
                GuardianDetails.objects.create(user=instance, **guardian_details_data)

        return instance

class CustomUserLoginSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not (username or email):
            raise serializers.ValidationError("Either username or email should be provided.")

        user = None

        if username:
            user = CustomUser.objects.filter(username=username).first()
        elif email:
            user = CustomUser.objects.filter(email=email).first()

        if not user or not user.check_password(password):
            raise serializers.ValidationError("Invalid email/username or password")

        data['user'] = user
        return data
