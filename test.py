import tkinter as tk
import time
import os
from PIL import Image, ImageTk

window = tk.Tk()

frameCount = 5
frames = [tk.PhotoImage(file = './gifs/idle.gif', format = 'gif -index %i' %(i)) for i in range(frameCount)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCount:
        ind = 0
    label.configure(image=frame)
    window.after(400, update, ind)

label = tk.Label()
label.pack()
window.after(0, update, 0)

window.mainloop()