import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image


root = tk.Tk()
root.geometry("400x400")


canvas = tk.Canvas(bg='black', relief='ridge')
canvas.grid(sticky='we')

label = tk.Label(canvas, text="Header", bg='black', fg='white')
label.grid(sticky='we', row=0, column=1, padx=(0,10))

canvas.grid_columnconfigure(1, weight=1)



# frame = tk.LabelFrame(root, text = "Frame 1", bg="cyan", padx=20, pady=20)
# frame.grid(padx=10, pady=10)

# button = tk.Button(frame, text="Press")
# button.pack()





root.mainloop()