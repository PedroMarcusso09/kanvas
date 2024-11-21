from django.urls import path
from .import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('accounts/', views.CreateAccountView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view()),
]