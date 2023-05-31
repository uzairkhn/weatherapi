import requests
import tkinter as tk

# Read the API key from the text file
with open("api_key.txt", "r") as file:
    api_key = file.read().strip()

# Create the tkinter window
window = tk.Tk()
window.geometry("400x300")
window.title("Weather App")
window.config(bg="#e0f2f1")  # Set background color

# Create the label to display the result
result_label = tk.Label(window, text="User Input:",
                        font=("Arial", 14), bg="#e0f2f1")
result_label.pack(pady=20)

# Custom styling for the label
result_label.config(relief=tk.RAISED, padx=10, pady=10)

# Create the function to get weather data


def get_weather():
    city_name = entry1.get()

    limit = 5
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    weather_data = requests.get(url).json()

    if len(weather_data) > 0:
        temp = int(weather_data["main"]["temp"] - 273.15)
        description = weather_data["weather"][0]["description"]
        main_weather = weather_data["weather"][0]["main"]

        output_text = f"Temperature: {temp:.2f}°C\n"
        output_text += f"Main Weather: {main_weather}\n"
        output_text += f"Description: {description}\n"
        result_label.config(text=output_text)
    else:
        result_label.config(text="Error retrieving weather data")


# Create the first Entry widget
entry1 = tk.Entry(window, font=("Arial", 12), width=30)
entry1.pack(pady=10)

# Custom styling for the entry widget
entry1.config(relief=tk.SOLID, bd=2)

# Create the button to get the input
button = tk.Button(window, text="Get Weather", font=(
    "Arial", 12), bg="#607d8b", fg="white", command=get_weather)
button.pack(pady=10)

# Custom styling for the button
button.config(relief=tk.FLAT, padx=10, pady=5)

# Run the tkinter event loop
window.mainloop()
