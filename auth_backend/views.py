from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
import jwt
import datetime
from django.db import IntegrityError

from auth_backend.serializer import UserRegistrationSerializer


def generate_jwt(user):
    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow(),
    }
    token = jwt.encode(payload, "secret", algorithm="HS256")

    return token


@api_view(["POST"])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except IntegrityError:
            return Response({"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "User registration successful"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def user_login(request):
    # if not request.user.is_authenticated:
    user = authenticate(username=request.data["email"], password=request.data["password"])
    if not user:
        return Response({"message": "User does not exist"}, status=status.HTTP_403_FORBIDDEN)
    login(request, user)
    token = generate_jwt(user)
    response = Response({"message": "User logged in"})
    response.set_cookie(
        key="jwt", value=token,
    )
    return response


@api_view(["GET"])
def user_logout(request):
    logout(request)
    response = Response({"message": "User logged out"})
    response.delete_cookie("jwt")
    return response
