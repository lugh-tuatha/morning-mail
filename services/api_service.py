import requests
from settings import Settings

class ApiService:
    def __init__(self):
        self.settings = Settings()

    def fetch_day_weather_forcast(self):
        parameters = {
            "lon": 121.774017,
            "lat": 12.879721,
            "cnt": 4,
            "appid": self.settings.APP_ID
        }

        response = requests.get(self.settings.API_BASE_URL, params=parameters)
        response.raise_for_status()
        data = response.json()
        return data["list"]
