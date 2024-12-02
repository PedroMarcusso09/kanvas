from rest_framework.generics import CreateAPIView
from .models import Account
from .serializers import AccountSerializer
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView


@extend_schema(
    tags=['Contas'],
    summary='Criação de usuário',
    description='Criar uma nova conta de usuário fornecendo username, password e email. O campo is_superuser é opcional',
)
class CreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


@extend_schema(
    tags=['Contas'],
    summary='Realizar login',
    description='Autenticação de usuários e obtenção de tokens JWT',
)
class CustomTokenObtainPairView(TokenObtainPairView):
    """View personalizada para login."""
    pass