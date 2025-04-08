from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from house_plant_hub_backend import views

urls = [
    path('admin/', admin.site.urls),
    path('input_reading/', views.input_reading, name="input_reading")
]

urlpatterns = [path("api/v1/", include(urls))]
