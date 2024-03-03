import random

from django.contrib.auth import get_user_model

from smscode.models import Code


User = get_user_model()


def generate_otp():
    return str(random.randint(10000000, 99999999))


def send_sms_otp(phone_number, otp):
    print(phone_number, '   ', otp)


def get_user_or_create(code_id):
    code = Code.objects.get(id=code_id)
    user = User.objects.get_or_create(username=code.phone_number,
                                      password=code.otp,
                                      first_name=code.username)
    return user

