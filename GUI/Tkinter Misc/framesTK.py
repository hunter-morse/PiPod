import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("320x240")
root.configure(bg='black')

canvas = tk.Canvas(root, bg='black', highlightbackground='black', relief='ridge')
canvas.grid(sticky='we')


header_left = tk.Label(canvas, text="L", bg='black', fg='white')
header_left.grid(sticky='w', row=0, column=0, padx=(25,0))

header_center = tk.Label(canvas, text="Header", bg='black', fg='white')
header_center.grid(sticky='we', row=0, column=1, padx=(0,0))

header_right = tk.Label(canvas, text="R", bg='black', fg='white')
header_right.grid(sticky='w', row=0, column=2, padx=(0,25))

canvas.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


class UniversalHeader(tk.Frame):
	"""
	Builds off of tk.Frame object. Customizable title. Always hosts play and wifi status.
	"""
	def __init__(self, parent, title_text):
		tk.Frame.__init__(self, parent)

		# Configure frame
		self.configure(bg='black')

		# Create header container
		header = tk.Canvas(self, bg='black', highlightbackground='black', relief='ridge')
		header.grid(sticky='we')

		# Create labels to put in header
		self.header_left = tk.Label(header, text="L", bg='black', fg='white')
		self.header_left.grid(sticky='w', row=0, column=0, padx=(25,0))

		self.header_center = tk.Label(header, text=title_text, bg='black', fg='white')
		self.header_center.grid(sticky='we', row=0, column=1, padx=(0,0))

		self.header_right = tk.Label(header, text="R", bg='black', fg='white')
		self.header_right.grid(sticky='w', row=0, column=2, padx=(0,25))

		# Configure header to span
		header.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(0, weight=1)

class MainMenuFrame(tk.Frame):
	def __init__(self, parent, title_text, elements):
		tk.Frame.__init__(self, parent)

		# Configure frame based on theme
		self.configure(bg='cyan')

		# Create header
		header = UniversalHeader(self, "Test Header")
		header.grid(row=0, columnspan=2, sticky='we')

		# Create menu container
		menu = tk.Canvas(self, bg='orange', highlightthickness=2, relief='groove')
		menu.grid(row=1, column=0, sticky='nswe')

		# Create scrollbar container
		scrollbar = tk.Canvas(self, bg='yellow', highlightthickness=2, relief='ridge', width=25)
		scrollbar.grid(row=1, column=1, sticky='ns')


		# Create menu items
		for i in range(len(elements)):
			option = tk.Label(menu, text=elements[i], justify=tk.LEFT, anchor='w', bg='green', fg='white')
			option.grid(row=i, column=0, sticky='we')

		menu.grid_columnconfigure(0, weight=1)

		self.grid_columnconfigure(0, weight=1)



window = tk.Tk()
window.geometry("320x240")

elements = ["option 0", "option 1", "option 2"]

mainMenu_frame = MainMenuFrame(window, "Test Header", elements)
mainMenu_frame.grid(row=0, column=0, sticky='nswe')
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)



# menu_frame = MenuPage(window, "Test Header")
# menu_frame.grid(row=0,column=0,sticky='nswe')
# window.grid_columnconfigure(0, weight=1)
# window.grid_rowconfigure(0, weight=1)



# frame = tk.LabelFrame(root, text = "Frame 1", bg="cyan", padx=20, pady=20)
# frame.grid(padx=10, pady=10)

# button = tk.Button(frame, text="Press")
# button.pack()





root.mainloop()
window.mainloop()