from tkinter import *

root = Tk()

# Callback functions
def btnClicked():
	my_label_btn = Label(root, text = "btn clicked")
	my_label_btn.grid(row = 3, column = 0)

# Create label widget
my_label1 = Label(root, text = "hello")
my_label2 = Label(root, text = "world")

# Buttons
my_button = Button(root, text = "enter", padx = 50, command = btnClicked)

# Show on screen
my_label1.grid(row = 0, column = 0)
my_label2.grid(row = 1, column = 0)
my_button.grid(row = 2, column = 0)


root.mainloop()