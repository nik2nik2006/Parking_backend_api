from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from rest_framework import serializers

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=12, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'mobile', 'first_name', 'is_active', 'is_staff')
        # fields = ('id', 'auth_token',)
        # read_only_fields = ('id', 'is_active', 'is_staff')


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'mobile', 'password', 'first_name')

    def validate_phone(self, value):
        user = User.objects.filter(mobile=value)
        if user:
            raise serializers.ValidationError("Phone is already taken")
        return value

    def validate_password(self, value):
        # password_validation.validate_password(value)
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
