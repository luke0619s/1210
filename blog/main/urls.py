from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('station/', views.station, name='station'),
    path('sort/', views.sort, name='sort'),
    path('sign/', views.sign, name='sign'),
    path('station_history/', views.station_history, name='station_history'),
    path('setting/', views.setting, name='setting'),
    path('upgrade_member/', views.upgrade_member, name='upgrade_member'),
    path('government_data/',views.government, name='government_data'),
    path('realtime/',views.realtime, name='realtime'),
    ]