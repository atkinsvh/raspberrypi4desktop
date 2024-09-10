import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import requests
import webbrowser

# Function to update the time on the clock tab
def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

# Function to get weather data using OpenWeatherMap API
def get_weather():
    api_key = 'a0c669945cefe2dd4a3503600956917e'  # Replace with your OpenWeatherMap API key
    city = 'Sarasota'  # You can set the city here or allow user input
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(weather_url)
    weather_data = response.json()

    if weather_data['cod'] == 200:
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        weather_label.config(text=f'{city}: {temp}°C, {description.capitalize()}')
    else:
        weather_label.config(text="Error fetching weather data")

# Function to handle YouTube search
def search_youtube():
    search_query = search_bar.get() or "cherry blossom tree lofi"  # Default search if no input
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)

# Initialize the Tkinter app
root = tk.Tk()
root.title("Cherry Blossom Dashboard")
root.geometry("800x480")  # Adjust according to your screen size

# Load and display background image (Cherry Blossom theme)
bg_image = Image.open("/home/neurolady/Desktop/RaspberryPiDesktop/cherry_blossom.png")  # Correct file path
bg_image = bg_image.resize((800, 480), Image.Resampling.LANCZOS)  # Resize to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)  # Fill the window with the background image

# Create the notebook (tabs)
tabControl = ttk.Notebook(root)

# Tabs for different functionalities
clock_tab = tk.Frame(tabControl, bg='light pink')  # Change to light pink for theme
weather_tab = tk.Frame(tabControl, bg='light pink')
calendar_tab = tk.Frame(tabControl, bg='light pink')
todo_tab = tk.Frame(tabControl, bg='light pink')
video_tab = tk.Frame(tabControl, bg='light pink')  # New tab for YouTube

# Add the tabs to the Notebook
tabControl.add(clock_tab, text='Clock')
tabControl.add(weather_tab, text='Weather')
tabControl.add(calendar_tab, text='Calendar')
tabControl.add(todo_tab, text='To Do List')
tabControl.add(video_tab, text="YouTube")

# Place the Notebook on top of the background
tabControl.pack(expand=1, fill='both')

# Clock tab content
clock_label = tk.Label(clock_tab, font=('Helvetica', 48), fg='white', bg='light pink', bd=0, highlightthickness=0)
clock_label.pack(pady=10)
update_clock()

# Weather tab content
weather_label = tk.Label(weather_tab, font=('Helvetica', 24), fg='white', bg='light pink', bd=0, highlightthickness=0)
weather_label.pack(pady=100)
get_weather()

# To Do List tab content (Placeholder)
todo_label = tk.Label(todo_tab, text="Your To-Do List here", font=('Helvetica', 24), fg='white', bg='light pink', bd=0, highlightthickness=0)
todo_label.pack(pady=100)

# YouTube tab content (Embedding a video)
youtube_label = tk.Label(video_tab, text="Embed your YouTube content or playlist here!", font=('Helvetica', 24), fg='white', bg='light pink')
youtube_label.pack(pady=10)

# Search and status bar (bottom part)
bottom_frame = tk.Frame(root, bg="light pink", bd=0, highlightthickness=0)
bottom_frame.pack(side="bottom", fill="x")

# Search bar and search button
search_bar = tk.Entry(bottom_frame, width=30)
search_bar.pack(side="left", padx=10, pady=10)
search_bar.insert(0, "cherry blossom tree lofi")  # Preload with default search query

search_button = tk.Button(bottom_frame, text="Search YouTube", bg="white", command=search_youtube)
search_button.pack(side="left", padx=5)

# Placeholder for battery and Wi-Fi icons
wifi_icon = tk.Label(bottom_frame, text="Wi-Fi", fg="white", bg="light pink")
wifi_icon.pack(side="right", padx=5)

battery_icon = tk.Label(bottom_frame, text="Battery: 40%", fg="white", bg="light pink")
battery_icon.pack(side="right", padx=5)

root.mainloop()
