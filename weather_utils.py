import datetime as dt

# Functions that use information from the API

# returns coordinates


def get_longitude_latitude(coordinate_x, coordinate_y):
    longitude = coordinate_x
    latitude = coordinate_y

    return round(longitude, 2), round(latitude, 2)

# kelvin to celsius/fahrenheit function


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32

    return round(celsius, 2), round(fahrenheit, 2)

# kelvin to celsius/fahrenheit (feels like) temperature


def feels_like_temperature_to_celsius_fahrenheit(feelsliketemp):
    feels_like_temp_celsius = feelsliketemp - 273.15
    feels_like_temp_fahrenheit = (feelsliketemp - 273.15) * 9/5 + 32

    return feels_like_temp_celsius, feels_like_temp_fahrenheit

# Unix to specific timezone (UTC timezone) ----- Implement American


def unix_to_specific_timezone(unix_timestamp, timezone_offset):
    local_time = dt.datetime.fromtimestamp(unix_timestamp)
    local_time_adjusted = local_time + dt.timedelta(seconds=timezone_offset)
    formatted_time = local_time_adjusted.strftime('%Y-%m-%d %H:%M:%S')

    return local_time, formatted_time


def unix_to_specific_timezone_sunset_sunrise(unix_sunrise, unix_sunset, timezone_offset):
    # sunrise
    local_time_sunrise = dt.datetime.fromtimestamp(unix_sunrise)
    local_time_sunrise_adjusted = local_time_sunrise + \
        dt.timedelta(seconds=timezone_offset)

    # sunset
    local_time_sunset = dt.datetime.fromtimestamp(unix_sunset)
    local_time_sunset_adjusted = local_time_sunset + \
        dt.timedelta(seconds=timezone_offset)

    # format time
    formatted_time_sunrise = local_time_sunrise_adjusted.strftime(
        '%Y-%m-%d %H:%M:%S')
    formatted_time_sunset = local_time_sunset_adjusted.strftime(
        '%Y-%m-%d %H:%M:%S')

    return formatted_time_sunrise, formatted_time_sunset, local_time_sunrise, local_time_sunset

# Function that returns windspeed as metric and imperial


def wind_speed_to_metric_imperial(windspeed):
    imperial_windspeed = windspeed * 2.23694
    metric_windspeed = windspeed

    return round(metric_windspeed, 2), round(imperial_windspeed, 2)

# returns weather descriptions


def extract_cloud_descriptions(response):
    descriptions = [entry['description'] for entry in response['weather']]

    return descriptions

# removes the characters when returning weather descriptions


def remove_characters(weather_description):
    weather_description_string = ', '.join(weather_description)

    return weather_description_string

# returns the name of the country from the API


def get_country_name(country_name):
    return country_name

# returns pressure


def get_pressure(pressure):
    return pressure

# returns humidity


def get_humidity(humidity):
    return humidity

# displays the information of the User's city they entered


def display_information(city, country, localized_time, temp_celsius, temp_fahrenheit, windspeed_metric, windspeed_imperial, humidity, lon, lat):
    city_information = f'{city}\nCity in {country}\n{localized_time}\n{temp_celsius}°C ({temp_fahrenheit}°F), WIND {windspeed_imperial} mph ({windspeed_metric} m/s), {humidity}% Humidity\nCoordinates: {lon}′N {lat}′W'

    return city_information
