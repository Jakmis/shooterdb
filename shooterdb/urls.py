from django.urls import path
from .api import api
from . import views

urlpatterns = [
    path('', views.home_view, name="index"),
    path('persons/', views.person_list_view, name='person_list'),
    path('person/<int:person_id>/', views.person_detail_view, name='person_detail'),
    path('clubs/', views.club_list_view, name="club_list"),
    path('clubs/<int:club_id>/', views.club_detail_view, name="club_detail"),
    path("api/", api.urls),
]