import tkinter as tk
from PIL import Image, ImageTk
import requests
import pyttsx3
import os

def fetch_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY", "8bb9dbb58ab6dc141b2e8de06e75bbc3")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = data.get('main', {}).get('temp')
        description = data.get('weather', [{}])[0].get('description')
        return temperature, description
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None, "Could not fetch weather data."

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def reset_to_static():
    image_label.config(image=images["static"])
    root.update()

def animate_speaking():
    image_label.config(image=images["speaking"])
    root.update()
    root.after(5000, reset_to_static)

def get_weather(event=None):
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city.")
        return

    temperature, description = fetch_weather(city)
    if temperature is not None:
        result_label.config(text=f"{city}: {temperature}°C, {description}")
        animate_speaking()
        speak_text(f"The current temperature in {city} is {temperature} degrees Celsius with {description}.")
    else:
        result_label.config(text=description)

root = tk.Tk()
root.title("HAPPY WEATHER WOMAN")

images = {}
try:
    images["static"] = ImageTk.PhotoImage(Image.open("img_woman/woman_stays.PNG"))
    images["speaking"] = ImageTk.PhotoImage(Image.open("img_woman/woman_talks.PNG"))
except FileNotFoundError as e:
    print(f"Error loading images: {e}")
    fallback_image = Image.new("RGB", (100, 100), color="red")
    images["static"] = ImageTk.PhotoImage(fallback_image)
    images["speaking"] = ImageTk.PhotoImage(fallback_image)

image_label = tk.Label(root, image=images["static"])
image_label.pack()

city_entry = tk.Entry(root, font=("Arial", 14), justify="center", relief="flat", bd=0)
city_entry.pack(pady=10)

fetch_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 14))
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

city_entry.bind('<Return>', get_weather)

try:
    root.mainloop()
except KeyboardInterrupt:
    print("Application closed.")