import tkinter as tk
from datetime import datetime

def time():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock.config(text = current_time)
    clock.after(1000, time)

def start_timer():
    global minutes
    global seconds
    global timer_running
    if not timer_running:
        timer_running = True
        minutes = int(input_minutes.get())
        seconds = minutes * 60
        countdown()

def pause_timer():
    global timer_running
    timer_running = False

def clear_timer():
    global minutes
    global seconds
    global timer_running
    timer_running = False
    minutes = 0
    seconds = 0
    timer.config(text = '00:00')

def countdown():
    global minutes
    global seconds
    global timer_running
    if seconds > 0 and timer_running:
        minutes, secs = divmod(seconds, 60)
        timer.config(text = '{:02d}:{:02d}'.format(minutes, secs))
        seconds -= 1
        timer.after(1000, countdown)
    elif seconds == 0:
        timer_running = False
        timer.config(text = '00:00')

root = tk.Tk()
root.title("Digital Clock")

clock = tk.Label(root, font = ("calibri", 40, "bold"), background = "purple", foreground = "white")
clock.pack(expand = True)
time()

input_minutes = tk.Entry(root)
input_minutes.pack()

start_button = tk.Button(root, text = "Start Timer", command = start_timer)
start_button.pack()

pause_button = tk.Button(root, text = "Pause Timer", command = pause_timer)
pause_button.pack()

clear_button = tk.Button(root, text = "Clear Timer", command = clear_timer)
clear_button.pack()

timer = tk.Label(root, font = ("calibri", 40, "bold"), background = "purple", foreground = "white")
timer.pack(expand = True)

timer_running = False

root.mainloop()
