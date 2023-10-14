import time
import math
import pyautogui
import tkinter as tk
import os 
import sys

from tkinter import ttk 
from PIL import Image, ImageTk

# Move the mouse to the initial position and click the mouse then make the circle
def circleTime():
    pyautogui.moveTo(x_initial, y_initial)
    time.sleep(2)

    for _ in range(num_steps+ 3):
        angle = (_ / num_steps) * 360
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(x, y, duration=total_time / num_steps)


    pyautogui.moveTo(x_initial, y_initial, duration=total_time / num_steps)

    pyautogui.mouseUp()

#mid ui
win = tk.Tk()
win.geometry("250x275")
win.title("Circle time")
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))   
imagedir = f"button.png"
original_image = Image.open(imagedir)
photo = ImageTk.PhotoImage(original_image)
ttk.Button(win, text="Click Here", image = photo, command=circleTime).pack(pady=20)

#actual program
width, height = pyautogui.size()
center_x, center_y = width/2, (height/2)+20 # +20 to account for the taskbar
radius = 140
total_time = .35
count = 0

#calculate the number of steps required to complete the circle
num_steps = int(total_time * 60)
angle_increment = 360 / num_steps

# Calculate the initial position
x_initial = center_x + radius
y_initial = center_y 



win.mainloop()