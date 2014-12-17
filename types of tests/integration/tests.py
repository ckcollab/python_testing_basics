import unittest
import requests
import json


def get_weather(city_name):
    return requests.get("http://api.openweathermap.org/data/2.5/weather?q=%s" % city_name)


class TestWeather(unittest.TestCase):
    def test_get_weather_returns_temp_min_and_max(self):
        result = get_weather("Coeur d'Alene, Idaho")
        data = json.loads(result.content)
        assert "temp" in data["main"]


if __name__ == "__main__":
    unittest.main()
