import pytest
from weather_report import as_snow_lover, as_sun_lover, report_weather

def test_report_weather():
    assert report_weather(24, as_sun_lover) == "not great"
    assert report_weather(25, as_sun_lover) == "great"
    assert report_weather(1, as_snow_lover) == "not great"
    assert report_weather(0, as_snow_lover) == "great"