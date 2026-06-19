import requests

city = input("Enter the city name: ")

api_key = "21b573fbdad936a12406cfd72bb185a9" # Replace with your OpenWeatherMap API key

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Error:", data["message"])

except requests.exceptions.RequestException as e:
    print("Network error:", e)