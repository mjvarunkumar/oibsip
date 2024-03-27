import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_condition = data["weather"][0]["description"]
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("Failed to fetch weather data. Please check your location or API key.")

def main():
    api_key = "b89804a0e605ee34c225976bacd16270"
    location = input("Enter city name or ZIP code: ")
    get_weather(api_key, location)

if __name__ == "__main__":
    main()

