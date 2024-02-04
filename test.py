import tkinter as tk
import random
from tkinter import ttk
from threading import Thread
from time import sleep
from PIL import Image, ImageTk, ImageSequence

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

impath = './bgifs/'

button_pressed = False
feed_button_pressed = False
pooped_times = 0

# Variables for progress bar
initial_progress = 50
progress_value = tk.DoubleVar(value=initial_progress)
progress_step = 1  # Adjust the decrement step
feed_increment = 10  # Adjust the increment when the feed button is pressed
decrement_interval = 1000  # Adjust the time interval for decrementing (in milliseconds)

# Function to decrement the progress bar slowly
def decrement_progress():
    current_value = progress_value.get()
    if current_value > 5:
        progress_value.set(current_value - progress_step)
    window.after(decrement_interval, decrement_progress)
    
# Function to handle feed button click
def feed_button_click():
    global feed_button_pressed
    feed_button_pressed = True
    current_value = progress_value.get()
    new_value = min(100, current_value + feed_increment)
    progress_value.set(new_value)

def on_loading(widget, value, loading_end):
    print('loading...')
    widget.start(150)
    sleep(15)
    widget.stop()
    value(100)
    on_ready()

def on_ready():
    print("now ready to work...")
    
def label_click(event):
    global button_pressed
    global pooped_times
    print("label clicked")
    button_pressed = True
    pooped_times += 1

def unpack_gif(src):
    # Load Gif
    image = Image.open(src)

    # Get frames and disposal method for each frame
    frames = []
    disposal = []
    for gifFrame in ImageSequence.Iterator(image):
        disposal.append(gifFrame.disposal_method)
        frames.append(gifFrame.convert('RGBA'))

    # Loop through frames, and edit them based on their disposal method
    output = []
    lastFrame = None
    thisFrame = None
    for i, loadedFrame in enumerate(frames):
        # Update thisFrame
        thisFrame = loadedFrame

        # If the disposal method is 2
        if disposal[i] == 2:
            # Check that this is not the first frame
            if i != 0:
                # Pastes thisFrame's opaque pixels over lastFrame and appends lastFrame to output
                lastFrame.paste(thisFrame, mask=thisFrame.split()[3])
                output.append(ImageTk.PhotoImage(lastFrame))
            else:
                output.append(ImageTk.PhotoImage(thisFrame))

        # If the disposal method is 1 or 0
        elif disposal[i] == 1 or disposal[i] == 0:
            # Appends thisFrame to output
            output.append(ImageTk.PhotoImage(thisFrame))

        # If disposal method is anything other than 2, 1, or 0
        else:
            raise ValueError('Disposal Methods other than 2: Restore to Background, 1: Do Not Dispose, and 0: No Disposal are supported at this time')

        # Update lastFrame
        lastFrame = loadedFrame

    return output

def event(cycle, check, event_number, x, y):
    global button_pressed
    global pooped_times
    global feed_button_pressed
    if feed_button_pressed or event_number == 300:
        check = 8
        event_number = 300
        window.after(100, update, cycle, check, event_number, x, y)
        feed_button_pressed = False
    elif button_pressed and pooped_times < 5:
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
        window.after(1000, update, cycle, check, event_number, x, y)
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
        if 20 < cycle < 67:
            x += 20
            y -= 15
        elif cycle >= 67:
            x -= 20
            y += 15
        cycle, event_number = gif_work(cycle, helicopter, event_number, 1,12)#go to idle or walk more
    elif check == 8:
        frame = feeding[cycle]
        cycle, event_number = gif_work(cycle, feeding, event_number, 3,12)#feeding
        
        

    # Ensure the window stays within the screen boundaries
    x = max(0, min(x, screen_width - 100))

    window.geometry('100x100+' + str(x) + '+'+ str(y))
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x, y)

# load in gifs
idle = [tk.PhotoImage(file=impath + 'idle.gif', format='gif -index %i' % i) for i in range(6)]
idle_to_sleep = [tk.PhotoImage(file=impath + 'sleep.gif', format='gif -index %i' % i) for i in range(7)]
sleep = [tk.PhotoImage(file=impath + 'sleeping.gif', format='gif -index %i' % i) for i in range(6)]
sleep_to_idle = [tk.PhotoImage(file=impath + 'wake.gif', format='gif -index %i' % i) for i in range(7)]
walk_positive = [tk.PhotoImage(file=impath + 'walkingleft.gif', format='gif -index %i' % i) for i in range(8)]
walk_negative = [tk.PhotoImage(file=impath + 'walkingright.gif', format='gif -index %i' % i) for i in range(8)]
poop = [tk.PhotoImage(file=impath + 'pooping.gif', format='gif -index %i' % i) for i in range(8)]


#helicopter_1 = [tk.PhotoImage(file=impath + 'helicopter_1.gif', format='gif -index %i' % i) for i in range(18)]
# helicopter_fast = [tk.PhotoImage(file=impath + 'helicopter_fast.gif', format='gif -index %i' % i) for i in range(9)]
# helicopter_fastest = [tk.PhotoImage(file=impath + 'helicopter_fastest.gif', format='gif -index %i' % i) for i in range(9)]
#tornado = [tk.PhotoImage(file=impath + 'TORNADO.gif', format='gif -index %i' % i) for i in range(3)]

helicopter_1 = unpack_gif(src=impath + 'helicopter_1.gif')
helicopter_fast = unpack_gif(src=impath + 'helicopter_fast.gif')
helicopter_fastest = unpack_gif(src=impath + 'helicopter_fastest.gif')
tornado = unpack_gif(src=impath + 'TORNADO.gif')

feeding = [tk.PhotoImage(file=impath + 'feeding.gif', format='gif -index %i' % i) for i in range(23)]
helicopter = [] + helicopter_1 + helicopter_fast + helicopter_fastest + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado
helicopter = helicopter + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado + tornado +  tornado 
print(len(helicopter))
# Window configuration

window.config(highlightbackground='#5a4e44')
# Set background color and remove border
window.configure(background='#5a4e44', highlightthickness=0)
label = tk.Label(window, bd=0, bg='#5a4e44')
window.overrideredirect(True)
#window.wm_attributes('-transparentcolor', '#5a4e44')
#window.wm_attributes('-transparent', '#5a4e44')

#draws on top
window.attributes('-topmost', True)
label.bind("<Button-1>", label_click)
label.pack()


# #progress bar stuff:
# # Progress Bar window configuration
# progress_window = tk.Toplevel(window)
# progress_window.title("Progress Bar")
# progress_window.attributes('-topmost', True)
# progress_window.geometry('96x96+' + str(0) + '+'+ str(y))

# # Dark purple outline
# progress_window.configure(bg='#3B1D57')

# # Create a style for the progress bar
# style = ttk.Style()
# style.configure("Purple.Horizontal.TProgressbar",
#                 thickness=30,  # Adjust thickness
#                 troughcolor='#3B1D57',  # Dark purple outline
#                 bordercolor='#3B1D57',  # Dark purple outline
#                 lightcolor='#8C7C9A',  # Light purple fill
#                 darkcolor='#8C7C9A',  # Light purple fill
#                 troughrelief='flat',  # Flat relief
#                 troughpadding=0)  # No padding

# progress_var = tk.DoubleVar()
# progress_bar = ttk.Progressbar(progress_window, variable=progress_var, length=100, mode='determinate', style="Purple.Horizontal.TProgressbar")
# progress_bar.pack(pady=20)


#### progress bar stuff

# Create a new Toplevel window for the progress bar
progress_window = tk.Toplevel(window)
progress_window.title("Progress Bar Window")
#progress_window.geometry('30x' + str(96) + '+0+0')  # Adjust the size and position of the window

progress_window.attributes('-topmost', True)
progress_window.geometry('30x120+' + str(0) + '+'+ str(y))
#progress_window.attributes('-alpha', 0.7) 
#progress_window.attributes("-transparentcolor", "black")  # Replace "black" with the color you want to be transparent
#progress_window.overrideredirect(True)  # Remove window borders

# Create an image for the feed button
feed_image = Image.open('feed_image.png')  # Replace 'feed_image.png' with the actual image file
feed_image = feed_image.resize((30, 30), Image.LANCZOS)  # Resize the image
feed_photo = ImageTk.PhotoImage(feed_image)

# Create a feed button with the feed image
feed_button = tk.Button(progress_window, image=feed_photo, command=feed_button_click, bd=0, bg='black')
feed_button.pack(side=tk.TOP, pady=0)

feed_button.image = feed_photo

# Create a label for the progress bar
#progress_label = ttk.Label(progress_window, text="Progress Bar", font=("Arial", 12))
progress_label = ttk.Label(progress_window)
progress_label.pack(side=tk.LEFT, pady=0)

# Create a style for the progress bar (pixel art style with light and dark purple colors)
style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", thickness=10, troughcolor="#6a5acd", bordercolor="#800080", background="#9370db")
#transparent?
#style.configure("TProgressbar", thickness=10, troughcolor="#6a5acd", bordercolor="#800080", background="#0000000")

# Create a progress bar
#progress_bar = ttk.Progressbar(progress_window, variable=progress_value, length=20, mode='determinate', orient='vertical', style="TProgressbar")
style = ttk.Style()
style.layout("TVertical.TProgressbar",
             [('Vertical.Progressbar.trough',
               {'children': [('Vertical.Progressbar.pbar',
                               {'side': 'top', 'sticky': 'ns'})],
                'sticky': 'nswe'}),
              ('Vertical.Progressbar.label', {'sticky': ''})])
progress_bar = ttk.Progressbar(progress_window, variable=progress_value, length=screen_height, mode='determinate', orient='vertical', style="TVertical.TProgressbar")
progress_bar.pack(side=tk.TOP, pady=0)

# Start the decrementing process
window.after(1, decrement_progress)

####Progress bar stuff end



# Loop the program
window.after(1, update, cycle, check, event_number, x, y)
window.mainloop()