import os
from dotenv import find_dotenv, load_dotenv
import requests
from pprint import pprint

env_file = find_dotenv('.env')
load_dotenv(env_file)

API_KEY = os.environ.get('API_KEY')

url = "https://api.openweathermap.org/data/2.5/weather"

kyiv_coordinates = {
    "lat": 50.4504,
    "lon": 30.5245
}


def get_weather(lat, lon):
        params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            response = requests.get(url, params=params)

            if response.status_code != 200:
                print(f"Error: {response.status_code} - {response.text}")
                return None

            weather_data = response.json()
            print(weather_data)

            temperature = weather_data.get('main', {}).get('temp', 'No temperature data available')
            description = weather_data.get('weather', [{}])[0].get('description', 'No description available')


            return {
                "description": description,
                "temperature": temperature
            }

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None


pprint(get_weather(kyiv_coordinates["lat"], kyiv_coordinates["lon"]))