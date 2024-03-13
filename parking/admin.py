from django.contrib import admin

from parking.models import Sale, ParkingSpace, Price

admin.site.register(ParkingSpace)
admin.site.register(Sale)
admin.site.register(Price)
