import tkinter as tk
import random

window = tk.Tk()

# Set screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#begin x
x = 200
#begin y
y = 700

cycle = 0
check = 1

idle_num = [1, 2, 3]
#if event number == 4, idle to sleep

walk_left = [5, 6, 7, 8]
walk_right = [9, 10, 11, 12]
sleep_num = [13, 14]
#if event number == 15, sleep to idle
event_number = random.randrange(1, 3, 1)

impath = './pgifs/'

button_pressed = False
pooped_times = 0

def label_click(event):
    global button_pressed
    global pooped_times
    print("label clicked")
    button_pressed = True
    pooped_times += 1

def event(cycle, check, event_number, x, y):
    global button_pressed
    global pooped_times
    if button_pressed and pooped_times < 5:
        check = 6
        event_number = 100
        window.after(100, update, cycle, check, event_number, x, y)
        button_pressed = False
    elif button_pressed and pooped_times == 5:
        check = 7
        event_number = 200
        window.after(100, update, cycle, check, event_number, x, y)
        button_pressed = False
        pooped_times = 0
    elif event_number in idle_num:
        check = 0
        print('idle')
        window.after(100, update, cycle, check, event_number, x, y)
    elif event_number == 4:
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
        window.after(500, update, cycle, check, event_number, x, y)
    elif event_number == 15:
        check = 3
        print('from sleep to idle')
        window.after(100, update, cycle, check, event_number, x, y)
    elif event_number == 100:
        check = 6
        print('button press poop')
        window.after(100, update, cycle, check, event_number, x, y)
    elif event_number == 200:
        check = 7
        print('HELICOPTER')
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
        cycle, event_number = gif_work(cycle, idle, event_number, 5, 11) # if idle, go to walking next
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 13, 13) #go to sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 14, 15) # if currently sleeping, sleep or wake
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1) # if wake, idle next
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 3, 12) #go to idle or walk more
        x -= 3
    elif check == 5:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 3,12)#go to idle or walk more
        x += 3
    elif check == 6:
        frame = poop[cycle]
        cycle, event_number = gif_work(cycle, poop, event_number, 1,12)#go to idle or walk more
    elif check == 7:
        frame = helicopter[cycle]
        if 30 < cycle < 50:
            x += 15
            y -= 12
        elif cycle >= 50:
            x -= 15
            y += 10
        cycle, event_number = gif_work(cycle, helicopter, event_number, 1,12)#go to idle or walk more
        

    # Ensure the window stays within the screen boundaries
    x = max(0, min(x, screen_width - 100))
    y = max(0, min(y, screen_width - 100))

    window.geometry('96x96+' + str(x) + '+'+ str(y))
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x, y)

# Call buddy's action gif
idle = [tk.PhotoImage(file=impath + 'idle.gif', format='gif -index %i' % i) for i in range(6)]
idle_to_sleep = [tk.PhotoImage(file=impath + 'sleep.gif', format='gif -index %i' % i) for i in range(7)]
sleep = [tk.PhotoImage(file=impath + 'sleeping.gif', format='gif -index %i' % i) for i in range(6)]
sleep_to_idle = [tk.PhotoImage(file=impath + 'wake.gif', format='gif -index %i' % i) for i in range(7)]
walk_positive = [tk.PhotoImage(file=impath + 'walkleft.gif', format='gif -index %i' % i) for i in range(8)]
walk_negative = [tk.PhotoImage(file=impath + 'walkright.gif', format='gif -index %i' % i) for i in range(8)]
poop = [tk.PhotoImage(file=impath + 'poop.gif', format='gif -index %i' % i) for i in range(8)]

helicopter_1 = [tk.PhotoImage(file=impath + 'helicopter_1.gif', format='gif -index %i' % i) for i in range(18)]
helicopter_slow = [tk.PhotoImage(file=impath + 'helicopter_slow.gif', format='gif -index %i' % i) for i in range(9)]
helicopter_fast = [tk.PhotoImage(file=impath + 'helicopter_fast.gif', format='gif -index %i' % i) for i in range(9)]
helicopter_faster = [tk.PhotoImage(file=impath + 'helicopter_faster.gif', format='gif -index %i' % i) for i in range(9)]
helicopter_fastest = [tk.PhotoImage(file=impath + 'helicopter_fastest.gif', format='gif -index %i' % i) for i in range(9)]
tornado = [tk.PhotoImage(file=impath + 'TORNADO.gif', format='gif -index %i' % i) for i in range(3)]

helicopter = [] + helicopter_1 + helicopter_slow + helicopter_fast + helicopter_fastest + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado 
helicopter = helicopter + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado
print(len(helicopter))
# Window configuration

# window.config(highlightbackground='black')
label = tk.Label(window, bd=0, bg='black')
# window.overrideredirect(True)
# window.wm_attributes('-transparentcolor', 'black')
# window.wm_attributes('-transparent', False)
label.bind("<Button-1>", label_click)
label.pack()

# Loop the program
window.after(1, update, cycle, check, event_number, x, y)
window.mainloop()