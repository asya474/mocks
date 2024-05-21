from weather_app import WeatherService
from mock_server import run_mock_server

def test_get_temperature_valid_city(mock_server):
    weather_service = WeatherService()
    temperature = weather_service.get_temperature("valid_city")

    expected_temperature = 20
    assert temperature == expected_temperature, f"Expected temperature: {expected_temperature}, Actual temperature: {temperature}"

def test_get_temperature_another_valid_city(mock_server):
    weather_service = WeatherService()
    temperature = weather_service.get_temperature("another_city")

    expected_temperature = 20
    assert temperature == expected_temperature, f"Expected temperature: {expected_temperature}, Actual temperature: {temperature}"

def test_get_temperature_error_response(mock_server):
    weather_service = WeatherService()
    temperature = weather_service.get_temperature("error_city")

    assert temperature is None, f"Expected temperature: None, Actual temperature: {temperature}"