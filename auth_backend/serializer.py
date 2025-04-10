from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, data):
        email = data["email"]
        username = email
        first_name = data["first_name"]
        last_name = data["last_name"]
        password = data["password"]

        user = get_user_model()

        new_user = user.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        new_user.set_password(password)
        new_user.save()

        return new_user
