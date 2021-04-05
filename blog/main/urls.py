from django.urls import path
from main import views
from django.conf.urls import url
from . import views

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
    url('bar/', views.ChartView.as_view(), name='bar'),
    url('bar2/', views.ChartView2.as_view(), name='bar2'),
    url('bar3/', views.ChartView3.as_view(), name='bar3'),
    url('bar4/', views.ChartView4.as_view(), name='bar4'),
    url('bar5/', views.ChartView5.as_view(), name='bar5'),
    url('bar6/', views.ChartView6.as_view(), name='bar6'),
    url('luke/', views.IndexView.as_view(), name='luke'),
    ]