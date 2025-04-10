import jwt
import sys
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer


def auth_middleware(get_response):
    def middleware(request):
        if (
            (
                request.path not in [
                    "/api/v1/register/",
                    "/api/v1/auth/login/",
                ]
            )
            and
            (
                "test" not in sys.argv
            )
        ):
            # Renders request
            response = Response(
                data={"message": "Not authenticated"}, status=status.HTTP_401_UNAUTHORIZED,
            )
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()

            token = request.COOKIES.get("jwt")

            if not token:
                # Checks is JWT token is present
                return response
            try:
                # Checks if JWT token has expired
                jwt.decode(token, "secret", algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                response.delete_cookie("jwt")
                return response

        return get_response(request)

    return middleware
