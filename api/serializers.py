from rest_framework import serializers

from parking.models import ParkingSpace, Sale


class ParkingSpaceSerializer(serializers.ModelSerializer):
    """Сериалайзер модели ParkingSpace."""
    # is_available = serializers.SerializerMethodField()

    class Meta:
        model = ParkingSpace
        fields = '__all__'
    #
    # def get_is_available(self, obj):
    #     if ParkingSpace.objects.get(pk = obj.pk,
    #                                 self.is_works):
    #         return True
    #     return False


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('id', 'user', 'parking', 'rent_from', 'rent_to', 'promo_code', 'datetime', 'price_amaunt')
        read_only_fields = ('user', 'parking')


class SaleCreatSerializer(serializers.ModelSerializer):
    """Сериалайзер создания модели Sale."""

    class Meta:
        model = Sale
        fields = '__all__'
