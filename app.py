# 1. Build a weather application that fetches weather data from a public API and displays the current weather and forecast for a specified location. - DONE
# You can add features like weather icons and temperature units conversion.
# 2. Use tkinter to make a GUI and display weather - IP
# 3. History - Pass all the information of the city and put it in an array or dictionary to rememeber which cities the user looked up. Also let the user be able to select between each one - IP
# IOS app store idea -- Add widget feature

import requests
import os
from dotenv import load_dotenv
from weather_utils import (
    kelvin_to_celsius_fahrenheit,
    unix_to_specific_timezone,
    wind_speed_to_metric_imperial,
    feels_like_temperature_to_celsius_fahrenheit,
    extract_cloud_descriptions,
    remove_characters,
    get_country_name,
    get_longitude_latitude,
    get_pressure, get_humidity,
    unix_to_specific_timezone_sunset_sunrise,
    display_information
)

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = input("Enter the name of a City: ")

# URL to access API
url = f"{BASE_URL}appid={API_KEY}&q={CITY}"

response = requests.get(url).json()

# Directly pass values to functions
# response[][] allows the program to extract data from the request and display them using the functions
coordinate_x, coordinate_y = get_longitude_latitude(
    response['coord']['lon'], response['coord']['lat'])
weather = remove_characters(
    extract_cloud_descriptions(response))
temp_to_celsius, temp_to_fahrenheit = kelvin_to_celsius_fahrenheit(
    response['main']['temp'])
feels_like_temp_celsius, feels_like_temp_fahrenheit = feels_like_temperature_to_celsius_fahrenheit(
    response['main']['feels_like'])
pressure = get_pressure(response['main']['pressure'])
humidity = get_humidity(response['main']['humidity'])
windspeed_to_metric, windspeed_to_imperial = wind_speed_to_metric_imperial(
    response['wind']['speed'])
localized_time, formatted_time = unix_to_specific_timezone(
    response['dt'], response['timezone'])
sunrise_time, sunset_time, formatted_time_sunrise, formatted_time_sunset = unix_to_specific_timezone_sunset_sunrise(
    response['sys']['sunrise'], response['sys']['sunset'], response['timezone'])
country = get_country_name(response['sys']['country'])

city_information = display_information(CITY, country, localized_time, temp_to_celsius,
                                       temp_to_fahrenheit, windspeed_to_metric, windspeed_to_imperial, humidity, coordinate_x, coordinate_y)


print(city_information)
