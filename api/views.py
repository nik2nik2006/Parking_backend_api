import random

import jwt
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import SendSMSGetSerializer, SendSMSSerializer, UserSerializer
from api.utils import generate_otp, send_sms_otp, get_user_or_create
from smscode.models import Code


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
        print('Register')
        user = get_user_or_create(code_id=code.id)
        print(user)
        serializer = UserSerializer(user)
        # user = register(request)
        # print(user)
        # print('Singin')
        # login(user.phone_number, user.password)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({'text': 'Всё супер! Код подошёл'},
        #                 status=status.HTTP_200_OK)

