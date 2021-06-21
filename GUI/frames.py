import tkinter as tk
from tkinter import ttk
from sys import platform

from PIL import ImageTk, Image

# Globals
KEY_UP 		= 8320768	# 111
KEY_DOWN	= 8255233	# 116
KEY_LEFT	= 8124162	# 113
KEY_RIGHT	= 8189699	# 114



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

class MenuFrame(tk.Frame):
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
		self.menuItems = []
		for i in range(len(elements)):
			option = tk.Label(menu, text=elements[i], justify=tk.LEFT, anchor='w', bg='green', fg='white')
			option.grid(row=i, column=0, sticky='we')
			self.menuItems.append(option)

		menu.grid_columnconfigure(0, weight=1)

		self.grid_columnconfigure(0, weight=1)

	def selectOption(self, index):
		if(self.menuItems[index].cget('bg') == 'green'):
			self.menuItems[index].configure(bg='blue')
		elif(self.menuItems[index].cget('bg') == 'blue'):
			self.menuItems[index].configure(bg='green')

def keyUpPressed(frame, index):
	newIndex = index - 1
	
	if(newIndex >= 0):
		oldOption = frame.menuItems[index]
		newOption = frame.menuItems[newIndex]
		oldOption.grid_forget()
		newOption.grid_forget()
		frame.selectOption(index)
		frame.selectOption(newIndex)
		oldOption.grid(row=index, column=0, sticky='we')
		newOption.grid(row=newIndex, column=0, sticky='we')

	else:
		pass

def keyDownPressed(frame, index):
	newIndex = index + 1
	
	if(newIndex < len(frame.menuItems)):
		oldOption = frame.menuItems[index]
		newOption = frame.menuItems[newIndex]
		oldOption.grid_forget()
		newOption.grid_forget()
		frame.selectOption(index)
		frame.selectOption(newIndex)
		oldOption.grid(row=index, column=0, sticky='we')
		newOption.grid(row=newIndex, column=0, sticky='we')


	else:
		pass


def keyPressed(event, frame, index):
	key = event.keycode
	print(key)
	if(key == KEY_UP):
		keyUpPressed(frame, index)
	elif(key == KEY_DOWN):
		keyDownPressed(frame, index)


window = tk.Tk()
window.geometry("320x240")

elements = ["option 0", "option 1", "option 2"]

mainMenu_frame = MenuFrame(window, "Test Header", elements)
mainMenu_frame.grid(row=0, column=0, sticky='nswe')
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

window.bind('<KeyPress>', lambda e: keyPressed(e, mainMenu_frame, 1))

mainMenu_frame.selectOption(1)



window.mainloop()