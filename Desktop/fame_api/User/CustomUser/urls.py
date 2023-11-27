from django.urls import path
from .views import SignUpView, LoginView, GuardianDetailsCreateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('guardian/', GuardianDetailsCreateView.as_view(), name='guardian-create'),
]
