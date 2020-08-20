from tkinter import *
import time
import random

root = Tk()
root.title("Bounce")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = Canvas(root,width=400,height=400,bd=0, highlightthickness=0)
canvas.configure(bg="Black")
canvas.pack()
root.update()
canvas.create_text(360,8,text="Score",fill="yellow",font=("Arial Black",15,))
global count
count = 0


class Ball:

	def __init__(self,canvas,paddle,color):
		self.canvas = canvas
		self.paddle = paddle
		self.id = canvas.create_oval(10,10,25,25,fill=color)
		print(self.id)
		self.canvas.move(self.id,245,100)
		start = [-3,-2,-1,0,1,2,3]
		random.shuffle(start)
		self.x = start[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()

	def hit_paddle(self,pos):

		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True
			return False
	def retry(self):
		return

	def draw(self):

		'''
		def arrow_left(event):
			self.x = -3
		def arrow_right(event):
			self.x = 3
		def arrow_up(event):
			self.y = -3
		def arrow_down(event):
			self.y = 3
		
		root.bind("<Left>",arrow_left)
		root.bind("<Right>",arrow_right)
		root.bind("<Up>",arrow_up)
		root.bind("<Down>",arrow_down)
		'''

		self.canvas.move(self.id,self.x,self.y)
		pos = self.canvas.coords(self.id)
		print(pos)
		if pos[1] <=0:
			self.y = 3
		if pos[3] >= self.canvas_height:
			self.y = 0
			self.x = 0
			canvas.create_text(200,200,text="Game Over",fill="magenta",font=("Arial Black",15))
		if pos[0] <= 0:
			self.x = 3
		if pos[2] >= self.canvas_width:
			self.x = -3
		if self.hit_paddle(pos) == True:
			global count
			self.y = -3
			a = canvas.create_text(360,30,text=count,fill="orange",font=("Arial Black",12))
			canvas.itemconfig(a,fill="black")
			count += 1
			a = canvas.create_text(360,30,text=count,fill="orange",font=("Arial Black",12))
			
class Paddle:

	def __init__(self,canvas,color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0,0,100,10,fill=color)
		print(self.id)
		self.canvas.move(self.id,150,380)
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all("<Left>",self.left)
		self.canvas.bind_all("<Right>",self.right)
	
	def draw(self):
		self.canvas.move(self.id,self.x,0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 0
		if pos[2] >= self.canvas_width:
			self.x = 0
	def right(self, evt):
		self.x = 8

	def left(self, evt):
		self.x = -8
		

paddle = Paddle(canvas,"blue")
ball = Ball(canvas,paddle,"red")
 

while 1:
	ball.draw()
	paddle.draw()
	root.update_idletasks()
	root.update()
	time.sleep(0.02)