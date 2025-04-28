import pytest
import requests_mock
from get_weather import get_weather
import requests


# Testing 200 status and JSON in response
def test_get_weather_success_status_code():
    with requests_mock.Mocker() as m:
        # Mocking a request with status code 200 and json response
        m.get("https://api.openweathermap.org/data/2.5/weather", status_code=200,
              json={"weather": [{"description": "clear sky"}], "main": {"temp": 22}})

        # Creating test request
        response = get_weather(50.4504, 30.5245)

        # Checking if request is not None
        assert response is not None

        # Checking if valid JSON in response
        assert response['description'] == 'clear sky'
        assert response['temperature'] == 22


# Testing 400 status and func response
def test_get_weather_failure_status_code():
    with requests_mock.Mocker() as m:
        # Mocking a request with status code 400
        m.get("https://api.openweathermap.org/data/2.5/weather", status_code=400,
              json={"weather": [{"description": "clear sky"}], "main": {"temp": 22}})

        # Creating test request
        response = get_weather(50.4504, 30.5245)

        # Getting None response from func
        assert response is None



# Mock get_weather func with invalid coordinates
def mock_get_weather(*args, **kwargs):
    response = requests.Response()
    response.status_code = 400
    response._content = b'{"cod":"400","message":"wrong latitude"}'
    return response

def test_get_weather_invalid_coordinates(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_get_weather)

    response = get_weather(9999, 9999)  # Incorrect values

    # Checking None response in func
    assert response is None



# Mock for an empty response from server
def mock_get_weather_empty_response(*args, **kwargs):
    response = requests.Response()
    response.status_code = 200
    response._content = b''  # Пустой ответ
    return response

def test_get_weather_empty_response(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_get_weather_empty_response)
    response = get_weather(50.4504, 30.5245)

    # Checking None response in func
    assert response is None




# Mock for server timeout
def mock_get_weather_timeout(*args, **kwargs):
    raise requests.exceptions.Timeout

def test_get_weather_timeout(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_get_weather_timeout)
    response = get_weather(50.4504, 30.5245)
    assert response is None