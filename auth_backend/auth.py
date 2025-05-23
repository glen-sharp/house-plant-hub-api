from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        user = UserModel.objects.get(username=username)

        if user.check_password(password):
            return user
        else:
            raise ValueError
