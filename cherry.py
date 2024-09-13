import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import requests
import subprocess
from io import BytesIO

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

# Function to handle YouTube search using Chromium on Raspbian Pi
def search_youtube():
    search_query = search_bar.get() or "cherry blossom tree lofi"  # Default search if no input
    url = f"https://www.youtube.com/results?search_query={search_query}"

    try:
        # Open Chromium with the YouTube search URL
        subprocess.run(['chromium-browser', url], check=True)
    except Exception as e:
        print(f"Error opening Chromium: {e}")

# Function to fetch cherry blossom images from the Unsplash API
def get_cherry_blossom_images():
    # Replace with your Unsplash API key
    unsplash_access_key = 'YOUR_UNSPLASH_API_KEY'
    url = f"https://api.unsplash.com/search/photos?query=cherry+blossom&client_id={unsplash_access_key}&per_page=10"
    response = requests.get(url)
    
    if 'results' in response.json():
        images = response.json()['results']
        return images
    else:
        print("Error: 'results' key not found in the response.")
        return []

# Function to display the next image in the slider
def display_next_image(images, current_index):
    if len(images) == 0:
        print("No images available to display.")
        return
    
    # Load the image from URL
    img_url = images[current_index]['urls']['regular']
    response = requests.get(img_url)
    img_data = Image.open(BytesIO(response.content))

    # Resize and display image for 800x480 screen (your screen size)
    img_data = img_data.resize((800, 480), Image.Resampling.LANCZOS)
    img_photo = ImageTk.PhotoImage(img_data)
    image_label.config(image=img_photo)
    image_label.image = img_photo

    # Schedule the next image to be displayed
    next_index = (current_index + 1) % len(images)  # Cycle through images
    root.after(5000, display_next_image, images, next_index)  # Update every 5 seconds

# Function to embed Google Calendar in Chromium
def open_calendar():
    calendar_url = "https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=America%2FNew_York&bgcolor=%23ffffff&src=MzdiZTY4YmQzOGJlYTg2OTU2NDZlNjhkNWM5M2JhMjZiMDYzY2ZjZWM1YzI5MGJjOTE4MzUyOTI2M2ZjY2QwMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=ZW4udXNhI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&color=%23D50000&color=%230B8043"
    
    try:
        # Open Chromium to display Google Calendar
        subprocess.run(['chromium-browser', calendar_url], check=True)
    except Exception as e:
        print(f"Error opening Chromium: {e}")

# To-Do List Functions
def add_task():
    task = todo_entry.get()
    if task:
        task_list.insert(tk.END, task)
        todo_entry.delete(0, tk.END)

def remove_task():
    try:
        task_list.delete(tk.ANCHOR)
    except Exception as e:
        print(f"Error removing task: {e}")

# Initialize the Tkinter app
root = tk.Tk()
root.title("Cherry Blossom Dashboard")
root.geometry("800x480")  # Set window size to match your screen

# Create the notebook (tabs)
tabControl = ttk.Notebook(root)

# Create tabs
clock_tab = ttk.Frame(tabControl)
weather_tab = ttk.Frame(tabControl)
calendar_tab = ttk.Frame(tabControl)
todo_tab = ttk.Frame(tabControl)
video_tab = ttk.Frame(tabControl)
image_tab = ttk.Frame(tabControl)  # New tab for the image slider

# Add the tabs to the Notebook
tabControl.add(clock_tab, text='Clock')
tabControl.add(weather_tab, text='Weather')
tabControl.add(calendar_tab, text='Calendar')
tabControl.add(todo_tab, text='To Do List')
tabControl.add(video_tab, text="YouTube")
tabControl.add(image_tab, text="Cherry Blossoms")

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

# Calendar tab content
calendar_label = tk.Label(calendar_tab, text="Open Google Calendar", font=('Helvetica', 24), fg='white', bg='light pink', bd=0, highlightthickness=0)
calendar_label.pack(pady=100)

# Button to open Google Calendar
calendar_button = tk.Button(calendar_tab, text="View Calendar", command=open_calendar, font=('Helvetica', 14))
calendar_button.pack(pady=10)

# To Do List tab content
todo_label = tk.Label(todo_tab, text="To-Do List", font=('Helvetica', 24), fg='white', bg='light pink')
todo_label.pack(pady=10)

# Entry field for adding tasks
todo_entry = tk.Entry(todo_tab, font=('Helvetica', 14))
todo_entry.pack(pady=10)

# Button to add tasks
add_button = tk.Button(todo_tab, text="Add Task", command=add_task, bg='white', font=('Helvetica', 14))
add_button.pack(pady=5)

# Task list (Listbox)
task_list = tk.Listbox(todo_tab, font=('Helvetica', 14), width=40, height=8)
task_list.pack(pady=10)

# Button to remove tasks
remove_button = tk.Button(todo_tab, text="Remove Selected Task", command=remove_task, bg='white', font=('Helvetica', 14))
remove_button.pack(pady=5)

# Cherry Blossom Image Slider content
image_label = tk.Label(image_tab, bg='light pink')
image_label.pack(pady=10)

# Fetch and display cherry blossom images
cherry_blossom_images = get_cherry_blossom_images()
display_next_image(cherry_blossom_images, 0)

# Global Search Bar at the bottom (applies to all tabs)
bottom_frame = tk.Frame(root, bg="light pink", bd=0, highlightthickness=0)
bottom_frame.pack(side="bottom", fill="x")

# Global search bar that stays at the bottom
search_bar = tk.Entry(bottom_frame, font=('Helvetica', 14), width=40)
search_bar.pack(side="left", padx=10, pady=10)

# Search button to trigger YouTube search globally
search_button = tk.Button(bottom_frame, text="Search YouTube", bg="white", font=('Helvetica', 14), command=search_youtube)
search_button.pack(side="left", padx=5)

# Battery and Wi-Fi icons
wifi_icon = tk.Label(bottom_frame, text="Wi-Fi", fg="white", bg="light pink")
wifi_icon.pack(side="right", padx=5)

battery_icon = tk.Label(bottom_frame, text="Battery: 40%", fg="white", bg="light pink")
battery_icon.pack(side="right", padx=5)

# Run the Tkinter main loop
root.mainloop()
