from tkinter import *
root = Tk()
root.title("Expression's Calculator")
root.geometry("700x100")
root.configure(background="#3bffe2")

def evaluate(event):
	data = e.get()
	ans.configure(text="Answer: "+str(eval(data)),font=("Arial black",15))
msg = Label(root,text="Enter Expression",font=("ALGERIAN",15)).pack()

e = Entry(root,width=45,borderwidth=5,font=("Arial black",15))
e.bind("<Return>",evaluate)
e.pack()

ans = Label(root,text="Answer: ",font=("",15))
ans.pack()
root.mainloop()