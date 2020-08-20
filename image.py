from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Basic Pythonic Image Viewer")

img1 = ImageTk.PhotoImage(Image.open("1.jpg").resize((540, 320), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("2.jpg").resize((540, 320), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open("cap1.jpg").resize((540, 320), Image.ANTIALIAS))
img4 = ImageTk.PhotoImage(Image.open("cap2.jpg").resize((540, 320), Image.ANTIALIAS))
img = [img1, img2,img3,img4]
#Image.open("File.jpg").resize((250, 250), Image.ANTIALIAS)

def next(image_number):
	global label
	label.grid_forget()
	label = Label(image=img[image_number])
	label.grid(row=0,column=0,columnspan=3)

	if(image_number == len(img)-1):
		nextBtn = Button(root, text=">>",state=DISABLED)
	else:
		nextBtn = Button(root, text=">>",command=lambda: next(image_number+1))

	if(image_number == 0):
		previousBtn = Button(root, text="<<",state=DISABLED)
	else:
		previousBtn = Button(root, text="<<",command=lambda: previous(image_number -1))

	previousBtn.grid(row=1,column=0)
	nextBtn.grid(row=1,column=2)

def previous(image_number):
	global label
	label.grid_forget()
	label = Label(image=img[image_number])
	label.grid(row=0,column=0,columnspan=3)
	
	if(image_number == len(img)-1):
		nextBtn = Button(root, text=">>",state=DISABLED)
	else:
		nextBtn = Button(root, text=">>",command=lambda: next(image_number+1))

	if(image_number == 0):
		previousBtn = Button(root, text="<<",state=DISABLED)
	else:
		previousBtn = Button(root, text="<<",command=lambda: previous(image_number -1))

	previousBtn.grid(row=1,column=0)
	nextBtn.grid(row=1,column=2)

#defining widgets
label = Label(image=img[0])
quitBtn = Button(root, text="Quit", command=root.quit)

nextBtn = Button(root, text=">>",command=lambda: next(1))
previousBtn = Button(root, text="<<",command=previous,state=DISABLED)

# placing on screen
label.grid(row=0,column=0,columnspan=3)
previousBtn.grid(row=1,column=0)
quitBtn.grid(row=1,column=1)
nextBtn.grid(row=1,column=2)

root. mainloop()