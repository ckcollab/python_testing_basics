import unittest
import requests
import json


def get_weather(city_name):
    return requests.get("http://api.openweathermap.org/data/2.5/weather?q=%s" % city_name)


class TestWeatherIntegration(unittest.TestCase):
    '''Many modules are tested together, any one point could fail or the API response
    could have changed since we last called it'''
    def test_get_weather_returns_temp(self):
        result = get_weather("Coeur d'Alene, Idaho")
        data = json.loads(result.content)
        assert "temp" in data["main"]

        # How could we improve this test? All it's looking for is the "temp" property to exist. We could also make sure
        # the returned value is of the right type!
        assert float(data["main"]["temp"])


if __name__ == "__main__":
    unittest.main()
