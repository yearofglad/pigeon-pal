import tkinter as tk
import time
import os
from PIL import Image, ImageTk

window = tk.Tk()
x = 0
window.geometry(f'100x100+{x}+200')  # Set window dimensions and initial position

frameCount = 8
frames = [tk.PhotoImage(file = './gifs/idle_to_sleep.gif', format = 'gif -index %i' %(i)) for i in range(frameCount)]


def update_position():
    global x
    x += 5  # Adjust the speed as needed
    window.geometry(f'100x100+{x}+200')  # Set window dimensions and position
    window.after(50, update_position)  # Schedule the next update after 50 milliseconds


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCount:
        ind = 0
    label.configure(image=frame)
    window.after(400, update, ind)


label = tk.Label()
label.pack()
update_position()
window.after(0, update, 0)

window.mainloop()