# treeview

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Window 1')

my_tree = ttk.Treeview(root)
my_tree["columns"] = ("Name", "ID")

# Format
my_tree.column("#0", width=120, minwidth = 25) 	# phantom column
my_tree.column("Name", anchor = W, width = 120, minwidth = 25)
my_tree.column("ID", anchor = CENTER, width = 120, minwidth = 25)

# Headings
my_tree.heading("#0", text = "Ghost", anchor = W)
my_tree.heading("Name", text = "Name", anchor = W)
my_tree.heading("ID", text = "ID", anchor = CENTER)

# Add data
my_tree.insert(parent = '', index = 'end', iid = 0, text = 'Parent', values = ('Hunter', 22))
my_tree.insert(parent = '', index = 'end', iid = 1, text = 'Parent', values = ('Finn', 23))
my_tree.insert(parent = '', index = 'end', iid = 2, text = 'Parent', values = ('Nick', 22))
my_tree.insert(parent = '', index = 'end', iid = 3, text = 'Parent', values = ('Will', 22))

# Add children
my_tree.insert(parent = 0, index = 'end', iid = 4, text = 'Child', values = ('Anna', 21))
my_tree.insert(parent = '', index = 'end', iid = 5, text = 'Child', values = ('Hatcher', 19))
my_tree.move('5', '1', '0')

# Pack
my_tree.pack(pady = 20)

root.mainloop()