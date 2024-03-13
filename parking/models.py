import datetime
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ParkingSpace(models.Model):
    """Модель описания парковочных мест."""
    number = models.CharField(max_length=256)
    description = models.TextField()
    is_works = models.BooleanField(default=True)
    discount_parking = models.DecimalField(max_digits=2,
                                           decimal_places=0,
                                           help_text='Скидка на парковочное место (от 0 до 99), проценты')
    image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return f'Парковочное место {self.number}'


class Sale(models.Model):
    """Модель парковочных мест к покупке."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales')
    parking = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    rent_from = models.DateField(null=False, blank=False)
    rent_to = models.DateField(null=False, blank=False)
    promo_code = models.CharField(max_length=64, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    price_amaunt = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'Пользователь: {self.user}, Место: {self.parking}, аренда до: {self.rent_to}'

    @staticmethod
    def price(price_type, price_amaunt):
        return int(price_type.amaunt)*price_amaunt


class Price(models.Model):
    """Модель стоимостей парковочных мест."""
    type_of_rental_interval = {
        'D': 'day',
        'M': 'month'
    }
    name = models.CharField(max_length=1, choices=type_of_rental_interval, default='M')
    amount = models.DecimalField(max_digits=6, decimal_places=0)
    will_act = models.DateField(null=False, blank=False, help_text='Начинает действовать с:')

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'will_act'),
                name='unique_price',
            ),
        )

    def __str__(self):
        return f'Продолжительность - {self.name}, стоимость - {self.amount}, начнёт дествовать с: {self.will_act}'
