from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", 'first_name']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(username=validated_data["username"],
                    first_name=validated_data["first_name"])
        user.set_password(validated_data["password"])
        user.save()
        return user
