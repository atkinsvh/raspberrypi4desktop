import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Japanese Cherry Blossom Dashboard")

tabControl = ttk.Notebook(root)

clock_tab = ttk.Frame(tabControl)
weather_tab = ttk.Frame(tabControl)
calendar_tab = ttk.Frame(tabControl)

tabControl.add(clock_tab, text='Clock')
tabControl.add(weather_tab, text='Weather')
tabControl.add(calendar_tab, text='Calendar')

# Clock tab
clock_label = tk.Label(clock_tab, font=('Helvetica', 48), fg='pink')
clock_label.pack(pady=20)
update_clock()

# Display background image (Cherry Blossom)
bg_image = Image.open("cherry_blossom.png")
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(relx=0.5, rely=0.5, anchor='center')

tabControl.pack(expand=1, fill='both')

root.mainloop()
