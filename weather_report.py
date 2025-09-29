def as_sun_lover(temperature):
    return "great" if temperature >= 25 else "not great"
def as_snow_lover(temperature):
    return "great" if temperature <= 0 else "not great"

def report_weather(temperature, sun_snow):
    return sun_snow(temperature)


print(report_weather(25, as_sun_lover))