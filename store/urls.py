from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.home, name="home"),
    path('newday/', views.newday, name="newday"),
    path('settings/', views.settings, name="settings"),
]
