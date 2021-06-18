from tkinter import *

window = Tk()
window.title("Window01")

window.geometry("400x400")

my_menu = Menu(window)
window.config(menu = my_menu)


# Commands
def cmd():
	my_label = Label(window, text = "Yee").pack()

def file_new():
	hide_all_frames()
	file_new_frame.pack(fill = "both", expand = 1)
	my_label = Label(file_new_frame, text = "File > New").pack()

def edit_cut():
	hide_all_frames()
	edit_cut_frame.pack(fill = "both", expand = 1)
	my_label = Label(edit_cut_frame, text = "Edit > Cut").pack()


def hide_all_frames():
	file_new_frame.pack_forget()
	edit_cut_frame.pack_forget()

# File menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = file_new)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = window.quit())

# Edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = edit_cut)
edit_menu.add_command(label = "Copy", command = cmd)
edit_menu.add_command(label = "Paste", command = cmd)


# Frame
file_new_frame = Frame(window, width = 400, height = 400, bg = "red")
edit_cut_frame = Frame(window, width = 400, height = 400, bg = "blue")

window.mainloop()