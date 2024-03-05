from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from rest_framework import serializers

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()
    # is_staff = serializers.BooleanField(source='user.is_staff')

    class Meta:
        model = User
        fields = ('id', 'phone', 'first_name', 'is_active', 'is_staff', 'auth_token')
        read_only_fields = ('id', 'is_active', 'is_staff')

    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'phone', 'password', 'first_name')

    def validate_phone(self, value):
        user = User.objects.filter(phone=value)
        if user:
            raise serializers.ValidationError("Phone is already taken")
        return value

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class EmptySerializer(serializers.Serializer):
    pass
