import tkinter as tk
import requests

API_KEY = '7a8ee580ffaab1f8638e539fb829829c'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get('cod') != 200:
            result_label.config(text="City not found.")
            return

        name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        wind = data['wind']['speed']

        result = f"📍 {name}, {country}\n🌡️ Temp: {temp}°C\n🌥️ Condition: {condition.title()}\n💨 Wind: {wind} m/s\n\nThank You For Visiting !!\n Have a great Day"
        result_label.config(text=result)

    except Exception as e:
        result_label.config(text=f"Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("Simple Weather App")
root.geometry("400x350")

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=25)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)
print("Thank You For Visiting !!\n Have a great Day")

root.mainloop()