from rest_framework.generics import CreateAPIView
from .models import Account
from .serializers import AccountSerializer


class CreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
