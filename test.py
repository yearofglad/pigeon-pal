import tkinter as tk
import random
import time
import os
from PIL import Image, ImageTk

window = tk.Tk()
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

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

# cycles through pictures
def update(ind, frameCount):
    frame = frames[ind]
    ind += 1
    if ind == frameCount:
        ind = 0
    label.configure(image=frame)
    window.after(400, update, ind, frameCount)  # Pass frameCount as an argument

label = tk.Label(window, bd=0, bg='black')
label.pack()

frames = []  # Initialize frames variable
changeAction()  # Start with an initial action
window.mainloop()