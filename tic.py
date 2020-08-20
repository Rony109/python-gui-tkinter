from tkinter import *
root = Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")
root.configure(bg="black")
# global counter to track the turn of player
global count, state, stop
state = [[0,0,0],[0,0,0],[0,0,0]]
count = 0
stop = False
global arr
arr  = list()
#canvas the play area
canvas = Canvas(root,width=300,height=300)
canvas.pack()
labelwin = Label(root,text="Tic Tac Toe",font=("arial black",20),fg="orange",bg="black")
labelwin.pack()
global labelwin1 
labelwin1 = Label(root,text=" ",font=("arial black",20),fg="orange",bg="black")
labelwin1.pack() 

class board:
	def __init__(self,canvas):
		global count
		self.canvas = canvas
		self.canvas.create_line(100,0,100,300,width=2)
		self.canvas.create_line(200,0,200,300,width=2)
		self.canvas.create_line(0,100,300,100,width=2)
		self.canvas.create_line(0,200,300,200,width=2)
		self.canvas.bind_all("<Button-1>",self.click)
	# to draw objects( shapes in this case)
	def draw_shape(self):
		# draw first column
		self.b1 = self.canvas.create_text(50,45,text=" ",font=("arial black",60),fill="black")
		#print(self.id)
		self.b2 = self.canvas.create_text(50,145,text=" ",font=("arial black",60),fill="black")
		#print(self.id)
		self.b3 = self.canvas.create_text(50,245,text=" ",font=("arial black",60),fill="black")
		#print(self.id)
		# draw second column
		self.b4 = self.canvas.create_text(150,45,text=" ",font=("arial black",60),fill="black")
		self.b5 = self.canvas.create_text(150,145,text=" ",font=("arial black",60),fill="black")
		self.b6 = self.canvas.create_text(150,245,text=" ",font=("arial black",60),fill="black")
		# draw third column
		self.b7 = self.canvas.create_text(250,45,text=" ",font=("arial black",60),fill="black")
		self.b8 = self.canvas.create_text(250,145,text=" ",font=("arial black",60),fill="black")
		self.b9 = self.canvas.create_text(250,245,text=" ",font=("arial black",60),fill="black")
		
		# here on click event the empty place is replaced by 'O' or 'X' depending on the turn of player 
	def click(self,event):
		global count, arr, stop
		d = {50:0,150:1,250:2,45:0,145:1,245:2}
		print(d)
		print("count :",count)
		pos = self.canvas.coords(CURRENT)
		print(pos)
		r = pos[0]
		c = pos[1]
		print("pos a ",r)
		print("pos bo ",c)

		#current specifies the current pointer of our cursor
		if self.canvas.find_withtag(CURRENT) and stop == False and state[d[r]][d[c]] == 0:
			if count%2 == 0:
				self.canvas.itemconfig(CURRENT, text="0",font=("arial black",60))
				count += 1
				arr.append([pos,"0"])
				state[d[r]][d[c]] = "0"
			else:
				self.canvas.itemconfig(CURRENT, text="X",font=("arial black",60))
				count += 1
				arr.append([pos,"X"])
				state[d[r]][d[c]] = "X"
		print(arr)
		print("state ", state)
		self.check_winner(state)

	def check_winner(self,state):
		
		global stop, labelwin1
		
		for i in range(3):
			if state[i][0] == state[i][1] == state[i][2] != 0:
				if state[i][0] == "X":
					print("player X won in row")
					labelwin1.configure(text="Player X won")
				else:
					print("player 0 won in row")
					labelwin1.configure(text="Player 0 won")
				stop = True


		for i in range(3):
			
			if state[0][i] == state[1][i] == state[2][i] != 0:
				if state[0][i] == "X":
					print("player X won in col")
					labelwin1.configure(text="Player X won")
				else:
					print("player 0 won in col")
					labelwin1.configure(text="Player 0 won")
				stop = True
			
		if state[0][0] == state[1][1] == state[2][2] != 0:
				if state[0][0] == "X":
					print("player X won in diagonal1")
					labelwin1.configure(text="Player X won")
				else:
					print("player 0 won in diagonal1")
					labelwin1.configure(text="Player 0 won")
				stop = True
			
		if state[0][2] == state[1][1] == state[2][0] != 0:
				if state[0][2] == "X":
					print("player X won in diagonal2")
					labelwin1.configure(text="Player X won")
				else:
					print("player 0 won in diagonal2")
					labelwin1.configure(text="Player 0 won")
				stop = True

b = board(canvas)
b.draw_shape()
#b.check_winner()
root.mainloop()