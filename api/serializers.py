from django.contrib.auth import get_user_model
from rest_framework import serializers

from smscode.models import Code

User = get_user_model()


class SendSMSGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['username', 'phone_number']


class SendSMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['session_token']
        read_only_fields = ['username', 'phone_number', 'session_token']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'password']
