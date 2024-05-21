import requests

class WeatherService:
    def get_temperature(self, city_name):
        response = requests.get(f"https://14e39e6e-78ef-4835-a0e3-b124f0a2789f.mock.pstmn.io/weather")
        data = response.json()
        temperature = data.get("temperature")
        return temperature