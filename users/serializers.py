from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from rest_framework import serializers

from parking.models import Sale

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=12, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
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


class SaleMinifieldSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели Sale для сериалайзера Пользователь.
    """

    class Meta:
        model = Sale
        fields = '__all__'


class UserWithSalesSerializer(serializers.ModelSerializer):
    """Сериалайзер модели User c продажами sale."""
    sales = serializers.SerializerMethodField()
    is_sales = serializers.SerializerMethodField()
    sales_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'mobile', 'password', 'first_name',
                  'is_sales', 'sales', 'sales_count')

    @staticmethod
    def get_sales(obj):
        sales = obj.sales.all()
        return SaleMinifieldSerializer(sales, many=True).data

    @staticmethod
    def get_sales_count(obj):
        return obj.sales.count()

    def get_is_sales(self, obj):
        if self.context['request'].user.is_anonymous:
            return False
        return Sale.objects.filter(
            user=self.context['request'].user,
        ).exists()
