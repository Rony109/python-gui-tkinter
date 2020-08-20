from tkinter import *
import time 
from random import randint

root = Tk()
root.title("MATRIX")
root.geometry("1000x500")
root.configure(bg="black")
label = Label(root,text="The Matrix",bg="#000000",fg="#09ff00",font=("Algerian",40))
label.pack()	

canvas = Canvas(root,height=500,width=1000, highlightthickness=0,highlightbackground="black")
canvas.configure(bg="black")
canvas.pack()

# Start with first three characters of Japanese Katakana syllabary
# Works like 0x30a0 - 0x30a9,0x30b0 - 0x30b9 upto g
#c3 = chr(0x30a0)
#c = chr(0x30a0 + randint(0,97))
#print(c)
#x,y =100,100 
#label = canvas.create_text(100,100,text=c, fill="#09ff00",font=("arial black",20))
def choose(n):
	c = chr(0x30a0 + randint(0,97))
	canvas.itemconfig(n,text=c)

def draw(i):
	c = chr(0x30a0 + randint(0,97))
	x,y =randint(0,1000),randint(0,10) 
	canvas.create_text(x,y,text=c, fill="#09ff00",font=("arial black",20))
	
	for j in range(100):
		choose(j)
		canvas.move(j,0,15)
		time.sleep(0.0001)
		root.update()
for i in range(100):	
	draw(i)
	
root.mainloop()