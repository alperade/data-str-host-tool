import json
import requests
import os
from keys import OPEN_WEATHER_API_KEY

def get_weather():
    params = {
        "lat": '41.62200002393113',
        "lon": '-74.77607566009745',
        "appid": OPEN_WEATHER_API_KEY,
        "units": "metric",
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params=params)
    try:
        content = json.loads(response.content)
        return {
            "temp": content["main"]["temp"],
            "weather": content["weather"][0]["main"]
        }
    except requests.HTTPError as e:
        print(f"Exception caught: {e}")

print(get_weather())
