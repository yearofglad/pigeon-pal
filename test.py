import tkinter as tk
import random
import time
import os
from PIL import Image, ImageTk

window = tk.Tk()

window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

x = 0
window.geometry(f'100x100+{x}+200')  # Set window dimensions and initial position

idle = [tk.PhotoImage(file = './gifs/idle.gif', format = 'gif -index %i' %(i)) for i in range(5)]
idle_to_sleep = [tk.PhotoImage(file = './gifs/idle_to_sleep.gif', format = 'gif -index %i' %(i)) for i in range(8)]
sleep_to_idle = [tk.PhotoImage(file = './gifs/sleep_to_idle.gif', format = 'gif -index %i' %(i)) for i in range(8)]
sleep = [tk.PhotoImage(file = './gifs/sleep.gif', format = 'gif -index %i' %(i)) for i in range(3)]
walking_negative = [tk.PhotoImage(file = './gifs/walking_negative.gif', format = 'gif -index %i' %(i)) for i in range(8)]
walking_positive = [tk.PhotoImage(file = './gifs/walking_positive.gif', format = 'gif -index %i' %(i)) for i in range(8)]

def changeAction():
    global frames  # Declare frames as a global variable
    event_number = random.randrange(1, 4, 1)  # Changed to 4 for correct range
    if event_number == 1:
        frames = idle
    elif event_number == 2:
        frames = sleep
    elif event_number == 3:
        frames = walking_negative
    update(0, len(frames))
    window.after(600, changeAction)

def update_position():
    global x
    x += 5  # Adjust the speed as needed
    window.geometry(f'100x100+{x}+200')  # Set window dimensions and position
    window.after(50, update_position)  # Schedule the next update after 50 milliseconds

def update(ind, frameCount):
    frame = frames[ind]
    ind += 1
    if ind == frameCount:
        ind = 0
    label.configure(image=frame)
    window.after(400, update, ind, frameCount)  # Pass frameCount as an argument

label = tk.Label()
label.pack()
update_position()
window.after(0, update, 0)

frames = []  # Initialize frames variable
changeAction()  # Start with an initial action
window.mainloop()