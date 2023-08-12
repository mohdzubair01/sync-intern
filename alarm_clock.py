import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time

def set_alarm():
    global alarm_time
    alarm_time_str = alarm_entry.get()
    try:
        alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid time format. Use HH:MM format.")
        return

    formatted_alarm_time = alarm_time.strftime("%I:%M %p")
    messagebox.showinfo("Alarm Set", f"Alarm set for {formatted_alarm_time}")

    threading.Timer(2, check_alarm).start()

def check_alarm():
    while True:
        current_time = datetime.now().time()
        if current_time >= alarm_time.time():
            messagebox.showinfo("Alarm", "ALARM! Wake up!")
            break
        time.sleep(1)

app = tk.Tk()
app.title("Alarm Clock")
app.geometry("300x150")

alarm_label = tk.Label(app, text="Set Alarm (HH:MM):")
alarm_label.pack()

alarm_entry = tk.Entry(app)
alarm_entry.pack()

set_alarm_button = tk.Button(app, text="Set Alarm", command=set_alarm)
set_alarm_button.pack()

app.mainloop()
