from django.urls import path
from .api import api
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", api.urls),
]