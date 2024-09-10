import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import requests

# Function to update the time on the clock tab
def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

# Function to get weather data using OpenWeatherMap API
def get_weather():
    api_key = 'a0c669945cefe2dd4a3503600956917e'  # Replace with your API key
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

# Initialize the Tkinter app
root = tk.Tk()
root.title("Cherry Blossom Dashboard")
root.geometry("800x480")  # Adjust according to your screen size

# Load and display background image (Cherry Blossom)
bg_image = Image.open("/home/neurolady/Desktop/RaspberryPiDesktop/mnt/data/cherry_blossom.png")  # Correct file path
bg_image = bg_image.resize((800, 480), Image.Resampling.LANCZOS)  # Resize the image to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)  # Fill the window with the background image

# Create the notebook (tabs)
tabControl = ttk.Notebook(root)

# Tabs for different functionalities (Using native Tkinter Frames)
clock_tab = tk.Frame(tabControl, bg='navy')  # Tkinter Frame instead of ttk.Frame
weather_tab = tk.Frame(tabControl, bg='navy')
calendar_tab = tk.Frame(tabControl, bg='navy')
todo_tab = tk.Frame(tabControl, bg='navy')

# Add the tabs to the Notebook
tabControl.add(clock_tab, text='Clock')
tabControl.add(weather_tab, text='Weather')
tabControl.add(calendar_tab, text='Calendar')
tabControl.add(todo_tab, text='To Do List')

# Place the Notebook on top of the background
tabControl.pack(expand=1, fill='both')

# Clock tab content (Including an image)
clock_label = tk.Label(clock_tab, font=('Helvetica', 48), fg='white', bg='navy', bd=0, highlightthickness=0)
clock_label.pack(pady=10)

# Load and display an image in the clock tab
clock_image = Image.open("/home/neurolady/Desktop/RaspberryPiDesktop/mnt/data/image.png")  # Correct file path
clock_image = clock_image.resize((150, 150), Image.Resampling.LANCZOS)  # Resize the image
clock_photo = ImageTk.PhotoImage(clock_image)
clock_image_label = tk.Label(clock_tab, image=clock_photo, bg='navy')
clock_image_label.pack(pady=10)

update_clock()

# Weather tab content
weather_label = tk.Label(weather_tab, font=('Helvetica', 24), fg='white', bg='navy', bd=0, highlightthickness=0)
weather_label.pack(pady=100)
get_weather()

# Load and display an image in the weather tab
weather_image = Image.open("/home/neurolady/Desktop/RaspberryPiDesktop/mnt/data/5.png")  # Correct file path
weather_image = weather_image.resize((150, 150), Image.Resampling.LANCZOS)
weather_photo = ImageTk.PhotoImage(weather_image)
weather_image_label = tk.Label(weather_tab, image=weather_photo, bg='navy')
weather_image_label.pack(pady=10)

# To Do List tab content (Placeholder)
todo_label = tk.Label(todo_tab, text="Your To-Do List here", font=('Helvetica', 24), fg='white', bg='navy', bd=0, highlightthickness=0)
todo_label.pack(pady=100)

# Load and display an image in the to-do list tab
todo_image = Image.open("/home/neurolady/Desktop/RaspberryPiDesktop/mnt/data/2.png")  # Correct file path
todo_image = todo_image.resize((150, 150), Image.Resampling.LANCZOS)
todo_photo = ImageTk.PhotoImage(todo_image)
todo_image_label = tk.Label(todo_tab, image=todo_photo, bg='navy')
todo_image_label.pack(pady=10)

# Search and status bar (bottom part)
bottom_frame = tk.Frame(root, bg="navy", bd=0, highlightthickness=0)
bottom_frame.pack(side="bottom", fill="x")

search_bar = tk.Entry(bottom_frame, width=30)
search_bar.pack(side="left", padx=10, pady=10)

search_button = tk.Button(bottom_frame, text="Search", bg="white")
search_button.pack(side="left", padx=5)

# Placeholder for battery and Wi-Fi icons
wifi_icon = tk.Label(bottom_frame, text="Wi-Fi", fg="white", bg="navy")
wifi_icon.pack(side="right", padx=5)

battery_icon = tk.Label(bottom_frame, text="Battery: 40%", fg="white", bg="navy")
battery_icon.pack(side="right", padx=5)

root.mainloop()
