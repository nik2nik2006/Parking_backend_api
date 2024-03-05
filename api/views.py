import random

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import QueryDict
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import SendSMSGetSerializer, SendSMSSerializer, UserSerializer
from api.utils import generate_otp, send_sms_otp
from smscode.models import Code
from users.serializers import UserCreateSerializer


User = get_user_model()


class SendSMSView(APIView):
    serializer_class = SendSMSGetSerializer

    def post(self, request):
        if not request.data['phone_number']:
            return Response({'errors': 'Номер телефона обязателен'},
                            status=status.HTTP_400_BAD_REQUEST)
        phone_number = request.data['phone_number']
        Code.objects.filter(phone_number=phone_number).delete()
        username = request.data['username']
        otp = generate_otp()
        data = {'phone_number': phone_number, 'nonce': random.random()}
        session_token = jwt.encode(data, settings.SECRET_KEY)
        code = Code.objects.create(phone_number=phone_number,
                                   username=username,
                                   otp=otp,
                                   session_token=session_token)
        send_sms_otp(phone_number, otp)
        serializer = SendSMSSerializer(code)
        # print('serializer.data = ', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifySMSView(APIView):
    serializer_class = SendSMSGetSerializer

    def post(self, request):
        if not request.data['session_token']:
            return Response('session_token is required')
        code = get_object_or_404(Code, session_token=request.data['session_token'])
        if int(request.data['otp']) != code.otp:
            return Response({'errors': 'Код проверки не верный'},
                            status=status.HTTP_400_BAD_REQUEST)
        print('Проверка прошла')
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # user = User.objects.create(serializer.validated_data)
        user = User.objects.create_user(username=request.data['username'],
                                        password=request.data['password'],
                                        commit=None,
                                        first_name=request.data['first_name'],
                                        otp=int(request.data['otp']))
        print(user)
        # serializer = UserCreateSerializer(data=)
        return Response(request.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({'text': 'Всё супер! Код подошёл'},
        #                 status=status.HTTP_200_OK)

