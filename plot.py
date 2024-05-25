import os
import time
import matplotlib.pyplot as plt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk

# Global variables to hold data
times = []
currents = []
voltages = []
last_line_read = 0  # To track the last read line

def read_data(filename):
    """
    Reads data from the specified file and updates global lists with new data.
    """
    global last_line_read
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            print(lines)
            if not lines:
                print("Warning: Empty file.")
                return

            # Process only new lines
            new_lines = lines[last_line_read:]
            for line in new_lines:
                time_interval, current, voltage = line.strip().split(",")
                times.append(float(time_interval))
                currents.append(float(current))
                voltages.append(float(voltage))
            
            # Update the last line read index
            last_line_read = len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading data: {e}")

def update_plot():
    """
    Updates the Matplotlib plot with the new data.
    """
    plt.clf()
    plt.plot(times, currents, label='Current (A)', color='blue')
    plt.plot(times, voltages, label='Voltage (V)', color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Values')
    plt.title('Real-time Data Plot')
    plt.legend()
    plt.grid(True)
    plt.draw()
    plt.pause(0.01)

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, root):
        self.root = root

    def on_modified(self, event):
        if event.src_path.endswith('.bak'):
            read_data(event.src_path)
            self.root.after(1, update_plot)

def monitor_file(filename, root):
    """
    Monitors the specified file for changes and updates the Matplotlib plot.
    """
    event_handler = FileChangeHandler(root)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    plt.ion()
    plt.figure(figsize=(10, 6))
    plt.show()

    try:
        root.mainloop()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    filename = "data.bak"
    root = tk.Tk()
    root.title("Real-time Data Plot")
    monitor_file(filename, root)
