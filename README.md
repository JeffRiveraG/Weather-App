# Weather App

This app allows the user to enter the name of a city, fetches weather data for that city from a public API (OpenWeatherMap.org), and presents the weather information in a formatted way, including temperature, wind speed, humidity, cloud description, and coordinates. The app also accounts for timezone adjustments to show the localized time for the city.

# Current Weather Information Available

1. Temperature: The current temperature in Celsius and Fahrenheit.
2. Feels Like Temperature: The temperature that the weather "feels like" in Celsius and Fahrenheit.
3. Wind Speed: The current wind speed in meters per second (m/s) and miles per hour (mph).
4. Humidity: The percentage of humidity in the air.
5. Cloud Description: The description of the cloud cover (e.g., "clear sky," "broken clouds," etc.).
6. Coordinates: The latitude and longitude coordinates of the city.

The app also provides additional features:

1. Timezone Adjustment: The app adjusts the timestamp received from the API to display the localized time for the city based on its timezone.
2. Data Conversion: The app converts temperature values from Kelvin to Celsius and Fahrenheit.
3. Wind Speed Conversion: The app converts wind speed values from meters per second (m/s) to miles per hour (mph).
4. Formatting: The app formats the weather information into a user-friendly display.

# Features to yet to be included

1. History - Pass all the information of the city and put it in an array or dictionary to rememeber which cities the user looked up. Also let the user be able to select between each one
2. Implement Tkinter
3. If possible, move to mobile app development and create widgets IOS/Andriod