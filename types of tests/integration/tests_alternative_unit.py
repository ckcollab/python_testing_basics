import unittest
import requests
import json
import responses


def get_weather(city_name):
    return requests.get("http://api.openweathermap.org/data/2.5/weather?q=%s" % city_name)


class TestWeatherIntegration(unittest.TestCase):
    '''Now we are testing very specifically that the get_weather function does what it
    is supposed to. The api could change but we're not testing the integration of the
    two.'''
    def test_get_weather_returns_temp_min_and_max(self):
        city_name = "Coeur d'Alene, Idaho"
        url = "http://api.openweathermap.org/data/2.5/weather?q=%s" % city_name
        data = json.dumps({
            "main":
            {
                "temp": 72.9
            }
        })
        responses.add(responses.GET,
                      url,
                      body=data,
                      content_type='application/json')

        result = get_weather(city_name)
        data = json.loads(result.content)
        assert "temp" in data["main"]


if __name__ == "__main__":
    unittest.main()
