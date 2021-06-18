from tkinter import *

root = Tk()

# Define entry
my_entry = Entry(root, width = 25)
my_entry.grid(row = 0, column = 0)
my_entry.insert(0, "type here")



def onClick():
	my_label = Label(root, text="entry: " + my_entry.get())
	my_label.grid(row = 3, column = 0)

my_button = Button(root, text = "click here", command = onClick)
my_button.grid(row = 1, column = 0)

root.mainloop()