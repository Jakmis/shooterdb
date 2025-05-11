from django.urls import path
from .api import api
from . import views

urlpatterns = [
    path('', views.home_view, name="index"),
    path('persons/', views.person_list_view, name='person_list'),
    path('person/<int:person_id>/', views.person_detail_view, name='person_detail'),
    path('person/create/', views.person_create_view, name='person_create'),
    path('clubs/', views.club_list_view, name="club_list"),
    path('clubs/<int:club_id>/', views.club_detail_view, name="club_detail"),
    path('clubs/create/', views.club_create_view, name="club_create"),
    path('competitions/', views.competition_list_view, name="competition_list"),
    path('competition/<int:pk>/', views.competition_detail_view, name="competition_detail"),
    path('competitions/create/', views.competition_create_view, name="competition_create"),
    path('result/create/', views.result_create_view, name='result_create'),
    path('guns/', views.gun_list_view, name='gun_list'),
    path('guns/create/', views.gun_create_view, name='gun_create'),
    path('trainer/create', views.trainer_create_view, name='trainer_create'),
    path("api/", api.urls),
]