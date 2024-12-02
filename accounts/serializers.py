from rest_framework import serializers
from accounts.models import Account
from rest_framework.validators import UniqueValidator


class AccountSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=Account.objects.all(),
            message='user with this email already exists.'
        )]          
    )

    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'email', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_superuser': {'required': False},
        }

    def create(self, validated_data: dict) -> Account:
        if validated_data.get('is_superuser', False):
            return Account.objects.create_superuser(**validated_data)

        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance