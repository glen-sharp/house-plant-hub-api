from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from house_plant_hub_backend import views
from auth_backend import views as auth_views

urls = [
    path("admin/", admin.site.urls),
    path("register/", auth_views.register_user, name="register"),
    path("auth/login/", auth_views.user_login, name="login"),
    path("auth/logout/", auth_views.user_logout, name="logout"),
    path("input_reading/", views.input_reading, name="input_reading"),
    path("readings/", views.readings, name="readings"),
]

urlpatterns = [path("api/v1/", include(urls))]
