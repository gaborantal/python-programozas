import utils

copied = utils.copy_list([2, 4, 6])

weather_szeged = {
    'city': 'Szeged',
    'temp': 12,
}

weather_budapest = {
    'city': 'Budapest',
    'temp': 10,
}

weather_forecast_list = [weather_szeged, weather_budapest]

weather_copy = utils.copy_list(weather_forecast_list)

weather_copy[0]['city'] = 'Swaged'

print('Eredeti lista', weather_forecast_list)
print('Másolat lista', weather_copy)
print('Eredeti Szegedi időjárás objektum', weather_szeged)

