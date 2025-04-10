import requests

def get_weather(city):
    api_key = '6e08078b1e62f2a8fd37233c6f1c8026'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data['cod'] != '404':
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        wind_speed = data['wind']['speed']

        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Weather Description: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"City {city} not found.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
