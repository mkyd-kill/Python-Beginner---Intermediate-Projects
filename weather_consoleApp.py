from requests.api import get

def format_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        feels_like = weather['main']['feels_like']
        wind = weather['wind']['speed']

        final_str = '\nCity: %s\nCountry: %s\nConditions: %s\nTemperature(°C): %s\nFeels Like(°C): %s\nWind Speed(Knots): %s' % (name, country, description, temperature, feels_like, wind)
    except Exception:
        final_str = "Sorry! There was a problem retrieving the information"

    return final_str

def get_weather(city):
    weather_key = 'f998d11d8b2f6a17ae1da5a1adf20b5f'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'APPID': weather_key,
        'q': city,
        'units': 'metric'
    }
    response = get(url, params=params)
    weather = response.json()
    label = format_response(weather=weather)

    return label#, weather

if __name__ == '__main__':
    try:
        city = str(input("Enter Name of City/Town\n:>> "))
        print(get_weather(city=city))
    except Exception:
        print("Error Detected During Data Retrievial.")