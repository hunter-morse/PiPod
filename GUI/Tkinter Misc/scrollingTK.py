import tkinter as tk
from tkinter import ttk

# Scrollable area is a frame within the canvas that moves up or down based on user scolling


# Applicaiton window
root = tk.Tk()

# Container for canvas and scrollbar
container = ttk.Frame(root)

# Canvas 
canvas = tk.Canvas(container)

# Scrollbar
scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)

# Scrollable frame
scroll_frame = ttk.Frame(canvas)

# Bind scrollable frame to canvas
# When scrollable frame changes size, change configuration of scroll properties
# canvas.bbox("all") returns a 4-value tuple containting defineing coordinates of the scroll box (2 corners)
scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window = scroll_frame, anchor = 'nw')
canvas.configure(yscrollcommand=scrollbar.set)

# Add elements to scroll_frame
for i in range(50):
	ttk.Label(scroll_frame, text="Sample scroll label").pack()


container.pack()
canvas.pack(side="left", fill="both")
scrollbar.pack(side="right", fill="y")


root.mainloop()