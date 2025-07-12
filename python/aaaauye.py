import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
from datetime import datetime, timedelta

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Full Clock App")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.create_clock_tab()
        self.create_timer_tab()
        self.create_stopwatch_tab()
        self.create_alarm_tab()

    # ------------------ CLOCK ------------------ #
    def create_clock_tab(self):
        self.clock_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.clock_tab, text="Clock")

        self.clock_label = tk.Label(self.clock_tab, font=('Helvetica', 48), fg='cyan', bg='black')
        self.clock_label.pack(expand=True, fill='both')

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.clock_label.after(1000, self.update_clock)

    # ------------------ TIMER ------------------ #
    def create_timer_tab(self):
        self.timer_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.timer_tab, text="Timer")

        self.timer_time = tk.StringVar(value="00:00:00")

        tk.Label(self.timer_tab, text="Set Timer (HH:MM:SS)").pack(pady=10)
        self.timer_entry = tk.Entry(self.timer_tab, textvariable=self.timer_time, justify="center", font=("Helvetica", 20))
        self.timer_entry.pack()

        self.timer_display = tk.Label(self.timer_tab, font=("Helvetica", 40), text="00:00:00")
        self.timer_display.pack(pady=20)

        tk.Button(self.timer_tab, text="Start Timer", command=self.start_timer).pack()

    def start_timer(self):
        time_str = self.timer_time.get()
        try:
            h, m, s = map(int, time_str.split(":"))
            total_seconds = h * 3600 + m * 60 + s
            self.countdown(total_seconds)
        except:
            messagebox.showerror("Invalid Format", "Use format HH:MM:SS")

    def countdown(self, total_seconds):
        if total_seconds > 0:
            self.timer_display.config(text=str(timedelta(seconds=total_seconds)))
            self.root.after(1000, lambda: self.countdown(total_seconds - 1))
        else:
            self.timer_display.config(text="Time's up!")
            messagebox.showinfo("Timer", "Time is up!")

    # ------------------ STOPWATCH ------------------ #
    def create_stopwatch_tab(self):
        self.stopwatch_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.stopwatch_tab, text="Stopwatch")

        self.sw_running = False
        self.sw_start_time = None
        self.sw_elapsed = 0

        self.sw_display = tk.Label(self.stopwatch_tab, text="00:00:00", font=("Helvetica", 40))
        self.sw_display.pack(pady=20)

        btn_frame = tk.Frame(self.stopwatch_tab)
        btn_frame.pack()

        tk.Button(btn_frame, text="Start", command=self.start_stopwatch).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Stop", command=self.stop_stopwatch).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Reset", command=self.reset_stopwatch).grid(row=0, column=2, padx=5)

    def update_stopwatch(self):
        if self.sw_running:
            elapsed_time = time.time() - self.sw_start_time + self.sw_elapsed
            formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            self.sw_display.config(text=formatted)
            self.root.after(1000, self.update_stopwatch)

    def start_stopwatch(self):
        if not self.sw_running:
            self.sw_start_time = time.time()
            self.sw_running = True
            self.update_stopwatch()

    def stop_stopwatch(self):
        if self.sw_running:
            self.sw_elapsed += time.time() - self.sw_start_time
            self.sw_running = False

    def reset_stopwatch(self):
        self.sw_running = False
        self.sw_start_time = None
        self.sw_elapsed = 0
        self.sw_display.config(text="00:00:00")

    # ------------------ ALARM ------------------ #
    def create_alarm_tab(self):
        self.alarm_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.alarm_tab, text="Alarm")

        tk.Label(self.alarm_tab, text="Set Alarm Time (HH:MM:SS)").pack(pady=10)
        self.alarm_time_var = tk.StringVar(value="00:00:00")
        self.alarm_entry = tk.Entry(self.alarm_tab, textvariable=self.alarm_time_var, font=("Helvetica", 20), justify="center")
        self.alarm_entry.pack()

        tk.Button(self.alarm_tab, text="Set Alarm", command=self.set_alarm).pack(pady=10)
        self.alarm_status = tk.Label(self.alarm_tab, text="No alarm set", fg="gray")
        self.alarm_status.pack()

    def set_alarm(self):
        alarm_time = self.alarm_time_var.get()
        try:
            datetime.strptime(alarm_time, "%H:%M:%S")
            self.alarm_status.config(text=f"Alarm set for {alarm_time}", fg="green")
            threading.Thread(target=self.check_alarm, args=(alarm_time,), daemon=True).start()
        except:
            messagebox.showerror("Invalid Format", "Use format HH:MM:SS")

    def check_alarm(self, alarm_time):
        while True:
            now = time.strftime("%H:%M:%S")
            if now == alarm_time:
                messagebox.showinfo("Alarm", f"It's {alarm_time}!")
                break
            time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
