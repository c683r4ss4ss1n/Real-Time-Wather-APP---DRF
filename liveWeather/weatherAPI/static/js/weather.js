$(document).ready(function () {
    $('#searchButton').click(function () {
        var city = $('#cityInput').val();
        if (city) {
            $.ajax({
                url: '/api/weather/?city=' + city,
                dataType: 'json',
                success: function (data) {
                    $('#city').text(data.city);
                    $('#temperature').text(data.temperature + ' °C');
                    $('#weatherDescription').text(data.weather_description);
                    $('#humidity').text(data.humidity + '%');
                    $('#windSpeed').text(data.wind_speed + ' m/s');
                },
                error: function () {
                    $('#weatherInfo').html('City not found');
                }
            });
        }
    });
});
