from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Images")
root.iconbitmap('calc_icon.ico')



# Image
my_img0 = ImageTk.PhotoImage(Image.open("./images/prof_img.png"))
my_img1 = ImageTk.PhotoImage(Image.open("./images/boxes_img.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("./images/stack_img.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("./images/jump_img.jpg"))

image_list = [my_img0, my_img1, my_img2, my_img3]

my_label =  Label(image = my_img0)
my_label.grid(row=2, column=0, columnspan = 3)

# Status Label
stat_label = Label(root, text = ( "Image %d of %d" %(1, len(image_list)) ), bd=1, relief=SUNKEN,  anchor = W)
stat_label.grid(row=0, column=0, columnspan=3, sticky = W+E)	# Sticky will stretch left to right (west to east)

# Button Functions
def imgScroll(image_number):
	global my_label
	global button_fwd
	global button_back

	print("b: %d, c: %d, n: %d" %((image_number-1)%len(image_list), image_number, (image_number+1)%len(image_list)))

	my_label.grid_forget()
	button_back.grid_forget()
	button_fwd.grid_forget()

	my_label = Label(image = image_list[image_number])
	button_fwd  = Button(root, text = " >> ", command = lambda: imgScroll((image_number+1)%len(image_list))) 
	button_back = Button(root, text = " << ", command = lambda: imgScroll((image_number-1)%len(image_list)))

	stat_label = Label(root, text = ( "Image %d of %d" %(image_number%len(image_list)+1, len(image_list)) ), bd=1, relief=SUNKEN,  anchor = W)
	stat_label.grid(row=0, column=0, columnspan=3, sticky = W+E)
	
	button_back.grid(row = 1, column = 0)
	button_fwd.grid(row = 1, column = 2)

	my_label.grid(row=2, column=0, columnspan = 3)




# Buttons
button_back = Button(root, text = " << ", command = lambda: imgScroll(-1))
button_quit = Button(root, text = "Exit", command = root.quit)
button_fwd  = Button(root, text = " >> ", command = lambda: imgScroll(1)) 

button_back.grid(row = 1, column = 0)
button_quit.grid(row = 1, column = 1)
button_fwd.grid(row = 1, column = 2)




root.mainloop()