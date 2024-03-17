from datetime import datetime

from rest_framework import serializers

from parking.models import ParkingSpace, Sale
from users.serializers import UserRegisterSerializer


class ParkingSpaceSerializer(serializers.ModelSerializer):
    """Сериалайзер модели ParkingSpace."""
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = ParkingSpace
        fields = '__all__'

    def get_is_available(self, obj):
        current_date = datetime.now().date()
        if Sale.objects.filter(
            parking=obj,
            rent_to__gt=current_date
            ).exists():
            return False
        return True


class SaleSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Sale."""
    user = UserRegisterSerializer()

    class Meta:
        model = Sale
        fields = ('id', 'user', 'parking', 'rent_from', 'rent_to', 'promo_code', 'datetime', 'price_amaunt')
        read_only_fields = ('user', 'parking')


class SaleCreatSerializer(serializers.ModelSerializer):
    """Сериалайзер создания модели Sale."""

    class Meta:
        model = Sale
        fields = '__all__'
