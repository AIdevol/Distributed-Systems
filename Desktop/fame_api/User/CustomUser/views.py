from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from CustomUser.models import CustomUser, GuardianDetails
from .serializer import CustomUserLoginSerializer, CustomUserSerializer, GuardianDetailsSerializer
from django.contrib.auth import authenticate

class SignUpView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()


            if user:
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                user_data = {
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'name': user.name,
                    'phone': user.phone,
                    'birthday': user.birthday,
                    'address': user.address,
                    'zip_code': user.zip_code,
                    'state': user.state,
                    'city': user.city,
                    'gender': user.gender,
                    'race': user.race,
                    'created_at': user.created_at,
                    'updated_at': user.updated_at,

                }

                if user.is_minor():
                    return Response({
                        'message': 'User created successfully. Please update guardian details as the user is a minor.'
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        'message': 'User created successfully',
                        'token': str(access_token),
                        'refresh_token': str(refresh),
                        'user_data': user_data,
                    }, status=status.HTTP_201_CREATED)

            return Response({'error': 'Unable to authenticate user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = CustomUserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data.get('user')

            if user:
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                user_data = {
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'name': user.name,
                    'phone': user.phone,
                    'birthday': user.birthday,
                    'address': user.address,
                    'zip_code': user.zip_code,
                    'state': user.state,
                    'city': user.city,
                    'gender': user.gender,
                    'race': user.race,
                    'created_at': user.created_at,
                    'updated_at': user.updated_at,
                }

                return Response({
                    'token': str(access_token),
                    'refresh_token': str(refresh),
                    'user_data': user_data,
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'error': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
    

class GuardianDetailsCreateView(generics.CreateAPIView):
    queryset = GuardianDetails.objects.all()
    serializer_class = GuardianDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        guardian_details, created = GuardianDetails.objects.get_or_create(user=user, defaults=serializer.validated_data)
        if not created:
            guardian_details.guardian_name = serializer.validated_data['guardian_name']
            guardian_details.save()

        return Response({"registered successfully"})