from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
import requests
from .serializers import WeatherSerializer
from django.shortcuts import render

class WeatherView(APIView):
    def get(self, request):
        city = request.query_params.get('city', 'YourDefaultCity')
        api_key = settings.WEATHER_API_KEY
        base_url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric',  # Use 'imperial' for Fahrenheit
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'weather_description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
            }
            serializer = WeatherSerializer(weather_data)
            return Response(serializer.data)
        else:
            return Response({'error': 'Weather data not found'}, status=404)


def weather(request):
    # Your view logic here
    context = {
        'city': 'New York',
        'temperature': '72°F',
        'weather_description': 'Sunny',
    }
    return render(request, 'weather.html', context)