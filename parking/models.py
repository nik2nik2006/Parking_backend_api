from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class ParkingSpace(models.Model):
    number = models.CharField(max_length=256)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    discount_parking = models.DecimalField(max_digits=2,
                                           decimal_places=0,
                                           help_text='Скидка на парковочное место (от 0 до 99), проценты')
    image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return f'Парковочное место {self.number}'


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    rented_before = models.DateField(null=False, blank=False)
    promo_code = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=16, decimal_places=0)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь: {self.user}, Место: {self.parking}, аренда до: {self.rented_before}'
