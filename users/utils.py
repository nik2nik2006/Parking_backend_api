from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


def get_and_authenticate_user(phone, password):
    user = authenticate(username=phone, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user


def create_user_account(phone, password, first_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        phone=phone, password=password,
        first_name=first_name, **extra_fields)
    return user
