from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    temperature = serializers.FloatField()
    weather_description = serializers.CharField()
    humidity = serializers.FloatField()
    wind_speed = serializers.FloatField()
