from tkinter import *

root = Tk()
root.title("Calculator")

# Global vars
addend_1 = None
op_flag = 0			# 0-nothing, 1-add, 2-subtrac

# Entry
e_user = Entry(root, width = 45, borderwidth = 5)
e_user.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

# Button Functions 
def button_pressed(value):
	current = e_user.get()
	e_user.delete(0, END)
	e_user.insert(0, str(current)+str(value))

def button_clear():
	e_user.delete(0, END)
	addend_1 = None
	op_flag = 0

def button_add(sign):
	global addend_1
	global op_flag
	current = e_user.get()
	num_dec = 0
	
	op_flag = sign

	if(addend_1 != None):
		addend_1 = button_equal()

	if('.' in current):
		num_dec = len(current)-current.index('.')
		addend_1 = float(current).round(num_dec)
		e_user.delete(0, END)
	
	else:
		if(current == ''):
			current = 0
		addend_1 = int(current)
		e_user.delete(0, END)


def button_equal():
	global addend_1
	global op_flag
	current = e_user.get()
	num_dec_cur = 0
	num_dec_add = 0
	sln = None
	
	e_user.delete(0, END)

	if('.' in current):
		num_dec_cur = len(current)-current.index('.')
		current = float(current).round(num_dec)
	else:
		current = int(current)

	if('.' in str(addend_1)):
		num_dec_add = len(addend_1)-addend_1.index('.')

	if(num_dec_add > num_dec_cur):
		if(op_flag == 1):
			sln = (round(addend_1 + current, num_dec_add))
		elif(op_flag == 2):
			sln = (round(addend_1 - current, num_dec_add))
		elif(op_flag == 3):
			sln = (round(addend_1 * current, num_dec_add))
		elif(op_flag == 4):
			sln = (round(addend_1 / current, num_dec_add))

	elif(num_dec_add < num_dec_cur):
		if(op_flag == 1):
			sln = (round(addend_1 + current, num_dec_cur))
		elif(op_flag == 2):
			sln = (round(addend_1 - current, num_dec_cur))
		elif(op_flag == 3):
			sln = (round(addend_1 * current, num_dec_cur))
		elif(op_flag == 4):
			sln = (round(addend_1 / current, num_dec_cur))

	elif(num_dec_add == num_dec_cur and num_dec_add > 0):
		if(op_flag == 1):
			sln = (round(addend_1 + current, num_dec_cur))
		elif(op_flag == 2):
			sln = (round(addend_1 - current, num_dec_cur))
		elif(op_flag == 3):
			sln = (round(addend_1 * current, num_dec_cur))
		elif(op_flag == 4):
			sln = (round(addend_1 / current, num_dec_cur))
			

	else:
		if(addend_1 is None):
			sln = int(current) 
		if(op_flag == 1):
			sln = (addend_1 + int(current))
		if(op_flag == 2):
			sln = (addend_1 - int(current))


	print(sln)
		
	e_user.insert(0, str(sln))

	op_flag = 0
	return(sln)




# Buttons
b_0 = Button(root, text = "0", padx = 90, pady = 20, command = lambda: button_pressed(0))
b_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_pressed(1))
b_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_pressed(2))
b_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_pressed(3))
b_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_pressed(4))
b_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_pressed(5))
b_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_pressed(6))
b_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_pressed(7))
b_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_pressed(8))
b_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_pressed(9))

b_plus    = Button(root, text = "+", padx = 39, pady = 20, command = lambda: button_add(1))
b_minus   = Button(root, text = "-", padx = 39, pady = 20, command = lambda: button_add(2))
b_mult    = Button(root, text = "+", padx = 39, pady = 20, command = lambda: button_add(3))
b_divide  = Button(root, text = "-", padx = 39, pady = 20, command = lambda: button_add(4))

b_decimal = Button(root, text = ".", padx = 39, pady = 20, command = lambda: button_pressed('.'))
b_equal   = Button(root, text = "=", padx = 39, pady = 20, command = button_equal)

b_clear	  = Button(root, text = "C", padx = 40, pady = 20, command = button_clear)

# On screen
b_9.grid(row = 1, column = 2)
b_8.grid(row = 1, column = 1)
b_7.grid(row = 1, column = 0)
b_clear.grid(row = 1, column = 3)

b_6.grid(row = 2, column = 2)
b_5.grid(row = 2, column = 1)
b_4.grid(row = 2, column = 0)
b_minus.grid(row = 2, column = 3)

b_3.grid(row = 3, column = 2)
b_2.grid(row = 3, column = 1)
b_1.grid(row = 3, column = 0)
b_plus.grid(row = 3, column = 3)

b_0.grid(row = 4, column = 0, columnspan = 2)
b_decimal.grid(row = 4, column = 2)
b_equal.grid(row = 4, column = 3)

b_mult.grid(row = 5, column = 2)
b_divide.grid(row = 5, column = 3)



root.mainloop()