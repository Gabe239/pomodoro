import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from PIL import Image
import serial
import time

if not hasattr(Image, 'CUBIC'):
    Image.CUBIC = Image.BICUBIC

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry('280x400')

        self.work_time = tk.IntVar(value=25)
        self.break_time = tk.IntVar(value=5)
        
        self.is_running = False
        self.is_work_session = True

        self.arduino = serial.Serial('COM3', 9600)  

        self.create_widgets()

    def create_widgets(self):
        tb.Label(self.root, text="Study Time (minutes):").grid(row=0, column=0, padx=5, pady=5)
        self.work_entry = tb.Entry(self.root, textvariable=self.work_time)
        self.work_entry.grid(row=0, column=1, padx=5, pady=5)

        tb.Label(self.root, text="Break Time (minutes):").grid(row=1, column=0, padx=5, pady=5)
        self.break_entry = tb.Entry(self.root, textvariable=self.break_time)
        self.break_entry.grid(row=1, column=1, padx=5, pady=5)

        self.start_button = tb.Button(self.root, text="Start", command=self.start_timer, bootstyle="success")
        self.start_button.grid(row=2, column=0, padx=5, pady=5)
        self.stop_button = tb.Button(self.root, text="Stop", command=self.stop_timer, state=tk.DISABLED, bootstyle="danger")
        self.stop_button.grid(row=2, column=1, padx=5, pady=5)

        self.timer_label = tb.Label(self.root, text="Timer: 00:00", font=("Helvetica", 24))
        self.timer_label.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.timer_meter = tb.Meter(
            master=self.root,
            bootstyle='info',
            subtext='Progress',
            interactive=False,
            stripethickness=10,
            metersize=200,
            amounttotal=100,
            amountused=0,
            textright='%', 
        )
        self.timer_meter.grid(row=4, column=0, columnspan=2, pady=10)

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.work_seconds = self.work_time.get() * 60
        self.break_seconds = self.break_time.get() * 60
        self.current_seconds = self.work_seconds if self.is_work_session else self.break_seconds
        self.total_seconds = self.current_seconds
        self.update_timer()
        

        self.arduino.write(b'S')  

    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        

        self.arduino.write(b'E')

    def update_timer(self):
        if self.is_running:
            minutes, seconds = divmod(self.current_seconds, 60)
            time_format = f"{minutes:01}:{seconds:01}"
            self.timer_label.config(text=f"Timer: {time_format}")

 
            elapsed_time = self.total_seconds - self.current_seconds
            progress_percentage = (elapsed_time / self.total_seconds) * 100
            self.timer_meter.configure(amountused=int(progress_percentage))  

            if self.current_seconds > 0:
                self.current_seconds -= 1
                self.root.after(1000, self.update_timer)
            else:
                if self.is_work_session:
                    self.arduino.write(b'E') 
                    messagebox.showinfo("Break Time", "Study session ended. Time for a break!")
                    self.current_seconds = self.break_seconds
                    self.total_seconds = self.break_seconds
                    self.is_work_session = False
                else:
                    self.arduino.write(b'S') 
                    messagebox.showinfo("Study Time", "Break session ended. Time to study!")
                    self.current_seconds = self.work_seconds
                    self.total_seconds = self.work_seconds
                    self.is_work_session = True
                self.update_timer()

if __name__ == "__main__":
    root = tb.Window(themename="darkly")
    pomodoro_timer = PomodoroTimer(root)
    root.mainloop()
