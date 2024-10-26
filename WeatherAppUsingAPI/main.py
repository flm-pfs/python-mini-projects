import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "your_openweathermap_api_key"  # Your OpenWeatherMap API key
# Base URL for the weather API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Get weather information for a given city.

    Args:
        city (str): The name of the city.

    Returns:
        tuple: A tuple containing temperature, humidity, and weather description.
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        return main['temp'], main['humidity'], weather['description']
    else:
        messagebox.showerror("Error", "City not found or API request failed.")
        return None, None, None


def display_weather():
    """
    Display the weather information for the entered city.
    """
    city = city_entry.get()
    temp, humidity, description = get_weather(city)
    if temp is not None:
        result_label.config(text=f"Temperature: {temp}°C\nHumidity: {
                            humidity}%\nDescription: {description}")


def main():
    """
    Main function to create the GUI and run the Weather App.
    """
    global city_entry, result_label
    root = tk.Tk()
    root.title("Weather App")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    city_label = tk.Label(frame, text="Enter City:", font=('Arial', 14))
    city_label.grid(row=0, column=0, padx=10)

    city_entry = tk.Entry(frame, width=20, font=('Arial', 14))
    city_entry.grid(row=0, column=1, padx=10)

    get_weather_button = tk.Button(frame, text="Get Weather", font=(
        'Arial', 14), command=display_weather)
    get_weather_button.grid(row=1, column=0, columnspan=2, pady=20)

    result_label = tk.Label(root, text="", font=('Arial', 14))
    result_label.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
