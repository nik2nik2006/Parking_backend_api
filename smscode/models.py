from django.db import models


class Code(models.Model):
    """Модель кодов. Поля: имя, номер_телефона, число, токен_сессии, создан, редактирован"""
    username = models.CharField(max_length=128, blank=True, null=True)
    phone_number = models.CharField(max_length=12, unique=True)
    otp = models.PositiveIntegerField()
    session_token = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Коды'
        verbose_name_plural = 'Коды'