import tkinter as tk
import random

window = tk.Tk()

# Set screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#begin x
x = 100
#begin y
y = 700

cycle = 0
check = 1

idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)

impath = './pgifs/'

def event(cycle, check, event_number, x, y):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update, cycle, check, event_number, x, y)
    elif event_number == 5:
        check = 1
        print('from idle to sleep')
        window.after(100, update, cycle, check, event_number, x, y)
    elif event_number in walk_left:
        check = 4
        print('walking towards left')
        window.after(100, update, cycle, check, event_number, x, y)
    elif event_number in walk_right:
        check = 5
        print('walking towards right')
        window.after(100, update, cycle, check, event_number, x, y)
    elif event_number in sleep_num:
        check = 2
        print('sleep')
        window.after(1000, update, cycle, check, event_number, x, y)
    elif event_number == 14:
        check = 3
        print('from sleep to idle')
        window.after(100, update, cycle, check, event_number, x, y)
    elif event_number == 100:
        check = 6
        print('pooping')
        window.after(100, update, cycle, check, event_number, x, y)

def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number

def update(cycle, check, event_number, x, y):
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)
    elif check == 1:
        frame = gotosleep[cycle]
        cycle, event_number = gif_work(cycle, gotosleep, event_number, 10, 10)
    elif check == 2:
        frame = sleeping[cycle]
        cycle, event_number = gif_work(cycle, sleeping, event_number, 10, 15)
        y += 20
    elif check == 3:
        frame = wakeup[cycle]
        cycle, event_number = gif_work(cycle, wakeup, event_number, 1, 1)
    elif check == 4:
        frame = walkingright[cycle]
        cycle, event_number = gif_work(cycle, walkingright, event_number, 1, 9)
        x -= 3
    elif check == 5:
        frame = walkingleft[cycle]
        cycle, event_number = gif_work(cycle, walkingleft, event_number, 1, 9)
        x += 3
    elif check == 6:
        frame = pooping[cycle]
        cycle, event_number = gif_work(cycle, pooping, event_number, 1, 15)
    
        
    # Ensure the window stays within the screen boundaries
    x = max(0, min(x, screen_width - 100))

    window.geometry('100x100+' + str(x) + '+'+ str(y))
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x, y)

def on_label_click(event):
    event_number = 100
    window.after(1, update, cycle, check, event_number, x, y)

# Call buddy's action gif
idle = [tk.PhotoImage(file=impath + 'idle.gif', format='gif -index %i' % i) for i in range(6)]
gotosleep = [tk.PhotoImage(file=impath + 'gotosleep.gif', format='gif -index %i' % i) for i in range(7)]
sleeping = [tk.PhotoImage(file=impath + 'sleeping.gif', format='gif -index %i' % i) for i in range(6)]
wakeup = [tk.PhotoImage(file=impath + 'wakeup.gif', format='gif -index %i' % i) for i in range(7)]
walkingright = [tk.PhotoImage(file=impath + 'walkingright.gif', format='gif -index %i' % i) for i in range(8)]
walkingleft = [tk.PhotoImage(file=impath + 'walkingleft.gif', format='gif -index %i' % i) for i in range(8)]
pooping = [tk.PhotoImage(file=impath + 'pooping.gif', format='gif -index %i' % i) for i in range(8)]


# Window configuration

# window.config(highlightbackground='black')
label = tk.Label(window, bd=0, bg='black')
# window.overrideredirect(True)
# window.wm_attributes('-transparentcolor', 'black')

# Pooping animation
label.bind('<Button-1>', on_label_click)
label.pack()

# Loop the program
window.after(1, update, cycle, check, event_number, x, y)
window.mainloop()

