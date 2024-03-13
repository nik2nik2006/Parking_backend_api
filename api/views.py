# from datetime import timedelta
import datetime
# from django.utils.timezone import datetime
from django.contrib.auth import get_user_model
# from django.db.models.functions import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import ParkingSpaceSerializer, SaleSerializer
from parking.models import ParkingSpace, Sale

User = get_user_model()


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(self):
        return Response({'message': 'Hello World!'}, status=status.HTTP_200_OK)


class ParkingSpaceViewSet(ModelViewSet):
    """Представление модели ParkingSpace."""
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    permission_classes = (AllowAny,)

    class Meta:
        model = ParkingSpace
        fields = '__all__'

    @action(detail=True, methods=['POST'],
            permission_classes=(IsAuthenticated,), pagination_class=None, serializer_class=SaleSerializer)
    def add_to_sale(self, request, **kwargs):
        parking = get_object_or_404(ParkingSpace, id=kwargs['pk'])
        sale = Sale.objects.filter(
                    parking=parking,
                    rent_to__gt=datetime.date.today()
        )
        if sale:
            return Response({'errors': f'Парковочное место с номером {sale[0].parking.number} сейчас занято.'
                                       f' Попробуйте позднее'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        sale = Sale.objects.create(
            user=request.user,
            parking=parking,
            rent_from=request.data['rent_from'],
            rent_to=request.data['rent_to'],
            promo_code=request.data['promo_code'],
            datetime=datetime.date.today(),
            price_amaunt=request.data['price_amaunt']
        )
        serializer = SaleSerializer(
            instance=sale
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SaleViewSet(viewsets.ModelViewSet):
    """Представление модели Sale."""
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (AllowAny,)

    class Meta:
        model = Sale
        fields = '__all__'
