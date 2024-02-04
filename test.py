import tkinter as tk
import random

window = tk.Tk()

# Set screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#begin x
x = 100
#begin y
y = 200

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
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= 3
    elif check == 5:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x += 3

    # Ensure the window stays within the screen boundaries
    x = max(0, min(x, screen_width - 100))
    y = max(0, min(y, screen_width - 100))

    window.geometry('96x96+' + str(x) + '+'+ str(y))
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x, y)

# Call buddy's action gif
idle = [tk.PhotoImage(file=impath + 'idle.gif', format='gif -index %i' % i) for i in range(6)]
idle_to_sleep = [tk.PhotoImage(file=impath + 'gotosleep.gif', format='gif -index %i' % i) for i in range(7)]
sleep = [tk.PhotoImage(file=impath + 'sleeping.gif', format='gif -index %i' % i) for i in range(6)]
sleep_to_idle = [tk.PhotoImage(file=impath + 'wakeup.gif', format='gif -index %i' % i) for i in range(7)]
walk_positive = [tk.PhotoImage(file=impath + 'walkingleft.gif', format='gif -index %i' % i) for i in range(8)]
walk_negative = [tk.PhotoImage(file=impath + 'walkingright.gif', format='gif -index %i' % i) for i in range(8)]

# Window configuration

# window.config(highlightbackground='black')
label = tk.Label(window, bd=0, bg='black')
# window.overrideredirect(True)
# window.wm_attributes('-transparentcolor', 'black')
label.pack()

# Loop the program
window.after(1, update, cycle, check, event_number, x, y)
window.mainloop()

