from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY:
        print("Error: API key not found. Check your .env file.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        # Task 2 — Handle rate limiting
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]

            print(f"{temp}°C, {condition}")

        elif response.status_code == 429:
            print("Too many requests. Please try again later.")

        elif response.status_code == 401:
            print("Invalid API key.")

        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Network error:", e)


if __name__ == "__main__":
    city = input("Enter city name: ")

    # Privacy Protection:
    # Do NOT log user location data (city name).
    # Logging location can expose sensitive personal information.
    # This violates data minimization principles under GDPR.

    get_weather(city)