from tkinter import *

root = Tk()

# Create label widget
my_label1 = Label(root, text = "hello")
my_label2 = Label(root, text = "world")

# Show on screen
my_label1.grid(row = 0, column = 0)
my_label2.grid(row = 1, column = 0)


root.mainloop()