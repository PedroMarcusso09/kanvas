from django.urls import path
from .views import CreateAccountView, CustomTokenObtainPairView

urlpatterns = [
    path('', CreateAccountView.as_view(), name='create-account'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
]
