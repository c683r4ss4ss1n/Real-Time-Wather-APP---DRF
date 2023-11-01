from django.urls import path
from .views import WeatherView, weather

urlpatterns = [
    path('weather/', WeatherView.as_view(), name='weather'),
    path('weathers/', weather, name='weather_template'),
]
