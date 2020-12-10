from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('station/', views.station, name='station'),
    path('sort/', views.sort, name='sort'),
    ]