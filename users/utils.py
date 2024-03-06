from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers


def get_and_authenticate_user(phone, password):
    user = authenticate(username=phone, password=password)
    if user is not None:
        try:
            token = Token.objects.get(user_id=user.id)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
        return user
    else:
        raise serializers.ValidationError("Invalid username/password. Please try again!")


def create_user_account(phone, password, first_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        phone=phone, password=password,
        first_name=first_name, **extra_fields)
    return user
