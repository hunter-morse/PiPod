import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image



# MainMenu inherits from tk.Frame
class MainMenu(tk.Frame):
	def __init__(self, master = None):
		super().__init__(self, master)
		
		# Set-up header container canvas to span full screen
		header_container = tk.Canvas(self, bg='black')
		header_container.grid(sticky='we')
		header_container.grid_columnconfigure(1, weight=1)

		# Organize header canvas
		self.header_label = tk.Label(header_container, text="Header", bg="black", fg="white")
		self.header_label.grid(sticky='we', row=0, column=1, padx=(0,10))



root = tk.Tk()

header_container = tk.Canvas(self, bg='black')
header_container.grid(sticky='we')
header_container.grid_columnconfigure(1, weight=1)





frame.pack()




root.mainloop()