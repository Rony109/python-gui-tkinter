from tkinter import *
import math
root = Tk()
root.title("Pythonic Calculator")
root["bg"] = "#000000"
root.iconbitmap("E:/python/gui/calculator.ico")
e = Entry(root,width=45,borderwidth=8,font=("Times New Roman",10))
e.grid(row = 0, column = 0, columnspan = 3)


def myclick(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def myequal():
	second_number = e.get()
	e.delete(0, END)
	if operation == "add":
		e.insert(0, fnum + int(second_number))
	if operation == "sub":
		e.insert(0, fnum - int(second_number))
	if operation == "mul":
		e.insert(0, fnum * int(second_number))
	if operation == "div":
		e.insert(0, fnum / int(second_number))


def calc(oper):
	first_num = e.get()
	e.delete(0, END)
	global fnum
	global operation
	fnum = int(first_num)
	operation = oper
	e.delete(0, END)

def mysqroot():
	val = math.sqrt(int(e.get()))
	e.delete(0,END)
	e.insert(0, val)

	return

def myac():
	e.delete(0, END)
	return


button_1 = Button(root, text="1",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(1))
button_2 = Button(root, text="2",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(2))
button_3 = Button(root, text="3",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(3))
button_4 = Button(root, text="4",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(4))
button_5 = Button(root, text="5",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(5))
button_6 = Button(root, text="6",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(6))
button_7 = Button(root, text="7",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(7))
button_8 = Button(root, text="8",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(8))
button_9 = Button(root, text="9",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(9))
button_0 = Button(root, text="0",bg="#333333",fg="#ffffff",padx=40,pady=15,command=lambda:myclick(0))

button_clear= Button(root, text="AC",bg="#874e04",fg="#ffffff",padx=36,pady=15,command=myac)
button_equal= Button(root, text="=",bg="#874e04",fg="#ffffff",padx=87,pady=15,command=myequal)

button_add= Button(root, text="+",bg="#01036e",fg="#ffffff",padx=40,pady=15,command=lambda:calc("add"))
button_sub= Button(root, text="-",bg="#01036e",fg="#ffffff",padx=40,pady=15,command=lambda:calc("sub"))
button_mul= Button(root, text="x",bg="#01036e",fg="#ffffff",padx=40,pady=15,command=lambda:calc("mul"))
button_div= Button(root, text="/",bg="#01036e",fg="#ffffff",padx=42,pady=15,command=lambda:calc("div"))
button_sqaureroot= Button(root, text="sq",bg="#01036e",fg="#ffffff",padx=35,pady=15,command=mysqroot)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=1)

button_add.grid(row=4,column=0)
button_sub.grid(row=4,column=2)
button_mul.grid(row=5,column=0)
button_div.grid(row=5,column=1)

button_clear.grid(row=6,column=0)
button_equal.grid(row=6,column=1,columnspan=2)
button_sqaureroot.grid(row=5,column=2)

root.mainloop()