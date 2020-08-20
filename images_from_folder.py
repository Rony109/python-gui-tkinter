import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog


root = Tk()
root.title("Basic Pythonic Image Viewer")

#img1 = ImageTk.PhotoImage(Image.open("1.jpg"))
#img2 = ImageTk.PhotoImage(Image.open("2.jpg"))
#img3 = ImageTk.PhotoImage(Image.open("cap2.jpg"))
#img4 = ImageTk.PhotoImage(Image.open("cap2.jpg"))
#img = [img1, img2,img3,img4]
#root.filename = filedialog.askopenfilename(initialdir="	/python/gui/images", title=" Select a file", filetypes=(("jpg files","* .jpg"),("All file types","*.*")))

path ="/python/gui/images"
print(path)
# changing the current working direcotry
os.chdir(path)

# reading all the files in Current working directory and storing in a list
img = [x for x in os.listdir()]
print("img is ",img)
global imgs
imgs = []
c = 0
for i in img:
	if((".jpg" in  i) or(".png" in  i) or (".PNG" in  i) or (".JPG" in  i)):
		print(i)
		image = Image.open(img[c]).resize((540, 320), Image.ANTIALIAS)
		imgs.append(ImageTk.PhotoImage(image))

		#imgs.append(ImageTk.PhotoImage(Image.open(img[c])))
		c+=1
print(imgs)


def select_folder():
	global imgs, label
	imgs = []
	path = root.dir = filedialog.askdirectory()
	print(path)
	# changing the current working direcotry
	os.chdir(path)

	# reading all the files in Current working directory and storing in a list
	img1 = [x for x in os.listdir()]
	print("img1", img1)
	imgs.clear()
	d = 0
	for i in img1:
		if((".jpg" in  i) or(".png" in  i) or (".PNG" in  i) or (".JPG" in  i)):
			print("one by one imgs",i)
			image = Image.open(i).resize((540, 320), Image.ANTIALIAS)
			imgs.append(ImageTk.PhotoImage(image))

			d+=1
	print(imgs)
	label.grid_forget()
	
	# Load everything again 
	
	label = Label(image=imgs[0])
	quitBtn = Button(root, text="Quit", padx=20, pady=10,command=root.quit)

	nextBtn = Button(root, text=">>",padx=20, pady=10,command=lambda: next(1))
	previousBtn = Button(root, text="<<",command=previous,padx=20, pady=10,state=DISABLED)
	lbl_path = Label(root,text=path,anchor=W).grid(row=3,column=0, padx=20, pady=10,columnspan=2)
	status = Label(root, text="image 1 of "+str(len(imgs)), anchor=E).grid(row=3, column = 2)

	# placing on screen
	label.grid(row=0,column=0,columnspan=3)
	previousBtn.grid(row=1,column=0)
	quitBtn.grid(row=1,column=1)
	nextBtn.grid(row=1,column=2)
	btn_file = Button(root,text="select folder",padx=100,pady=10, command=select_folder)
	btn_file.grid(row=2,column=0,columnspan=3)



def next(image_number):
	global label
	label.grid_forget()
	label = Label(image=imgs[image_number])
	label.grid(row=0,column=0,columnspan=3)

	if(image_number == len(imgs)-1):
		nextBtn = Button(root, text=">>",padx=20, pady=10,state=DISABLED)
	else:
		nextBtn = Button(root, text=">>",padx=20, pady=10,command=lambda: next(image_number+1))

	if(image_number == 0):
		previousBtn = Button(root, text="<<",padx=20, pady=10,state=DISABLED)
	else:
		previousBtn = Button(root, text="<<",padx=20, pady=10,command=lambda: previous(image_number -1))

	status = Label(root, text="image "+str(image_number+1)+" of "+str(len(imgs)), anchor=E).grid(row=3, column = 2)
	previousBtn.grid(row=1,column=0)
	nextBtn.grid(row=1,column=2)


def previous(image_number):
	global label
	label.grid_forget()
	label = Label(image=imgs[image_number])
	label.grid(row=0,column=0,columnspan=3)
	
	if(image_number == len(imgs)-1):
		nextBtn = Button(root, text=">>",padx=20, pady=10,state=DISABLED)
	else:
		nextBtn = Button(root, text=">>",padx=20, pady=10,command=lambda: next(image_number+1))

	if(image_number == 0):
		previousBtn = Button(root, text="<<",padx=20, pady=10,state=DISABLED)
	else:
		previousBtn = Button(root, text="<<",padx=20, pady=10,command=lambda: previous(image_number -1))

	status = Label(root, text="image "+str(image_number+1)+" of "+str(len(imgs)), anchor=E).grid(row=3, column = 2)
	previousBtn.grid(row=1,column=0)
	nextBtn.grid(row=1,column=2)


#defining widgets
label = Label(image=imgs[0])
quitBtn = Button(root, text="Quit", padx=20, pady=10,command=root.quit)

nextBtn = Button(root, text=">>",padx=20, pady=10,command=lambda: next(1))
previousBtn = Button(root, text="<<",command=previous,padx=20, pady=10,state=DISABLED)
lbl_path = Label(root,text=path,anchor=W).grid(row=3,column=0, padx=20, pady=10,columnspan=2)
status = Label(root, text="image 1 of "+str(len(imgs)), anchor=E).grid(row=3, column = 2)
# placing on screen
label.grid(row=0,column=0,columnspan=3)
previousBtn.grid(row=1,column=0)
quitBtn.grid(row=1,column=1)
nextBtn.grid(row=1,column=2)
btn_file = Button(root,text="select folder",padx=100,pady=10, command=select_folder)
btn_file.grid(row=2,column=0,columnspan=3)

root. mainloop()