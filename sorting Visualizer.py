from tkinter import *
from random import randint
import random
import time
root = Tk()
root.geometry("450x480")
root.title("See the Sorting!!!")
root.configure(bg="#0a0a0a")
root.iconbitmap("E:/python/gui/sort.ico")
width = 400
height = 300

canvas = Canvas(root, width=400, height=300)
canvas.pack(padx=10,pady=10)
canvas.configure()

frame1 = Frame(root,width=400,height=50)
frame1.config(bg="#141414")
frame1.pack(padx=10,pady=10)

frame2 = Frame(root,width=400,height=100)
frame2.config(bg="#141414")
frame2.pack(padx=10,pady=10)

num = 10
w = 1
global values
values = []	
def gen1():
	global values
	values = [1,2,3,4,5,6,7,8,9,10]
	canvas.delete("all")
	random.shuffle(values)
	#height = 300/len(values)
	#for i in range(0,num):
	#	values.append(randint(1,num))
	print("before sorting",values)
	
	offset = 40
	spacing = 4
	width = (300/len(values))+1
	for i in range(0,len(values)):
		x1 = (i*width)+offset+spacing
		x2 = ((values[i]))*20
		y1 = (i+1)*width + offset
		y2 = 400
		
		canvas.create_rectangle(x1,x2,y1,y2,fill="red")
		canvas.create_text(x1+width/3,x2+(x2/3),text=len(values)-values[i]+1,fill="Black")
		

def sort(x):
	global values
	canvas.delete("all")
	
	if not values:
		print("List is empty")
		canvas.create_text(width/2,height/2,text="Generate\nArray",font=("Algerian",40),fill="BLUE")
	else:
		
		n = len(values)

		if x==1: #BUBBLE SORT
			for i in range(0,n-1): 
				for j in range(0,n-i-1): 
			
					if values[j] > values[j+1] : 
						values[j], values[j+1] = values[j+1], values[j] 
						sortviz(values,["blue" if x == j or x == j+1 else "red" for x in range(len(values)) ])
						time.sleep(0.2)
			sortviz(values,["green" for x in range(len(values))])
						
		#SELECTION SORT
		elif x==2:
			for i in range(len(values)):
				min_idx = i
				for j in range(i+1,len(values)):
					if values[min_idx] > values[j]:
						print(values)
						min_idx = j
				values[i], values[min_idx] = values[min_idx], values[i] 
				sortviz(values,["blue" if x == i or x == min_idx else "red" for x in range(len(values))])
				time.sleep(0.1)
			sortviz(values,["green" for x in range(len(values))])
			print(values)
				
		elif x==3:	#QUICK SORT
		
			def partition(arr,low,high): 
			    i = ( low-1 )         # index of smaller element 
			    pivot = arr[high]     # pivot 
			    sortviz(arr,["yellow" if x == pivot else "red" for x in range(len(values)) ])
			            
			    for j in range(low , high): 
			        if   arr[j] < pivot: 
			            i = i+1 
			            arr[i],arr[j] = arr[j],arr[i]
			            #sortviz(arr,["orange" if x == low or x == pivot else "red" for x in range(len(values)) ])
			            #time.sleep(1) 
			             
			    arr[i+1],arr[high] = arr[high],arr[i+1]
			    #sortviz(arr,["yellow" if x == i or x == i+1 else "red" for x in range(len(values))])
			    #sortviz(arr,["yellow" if x == i or x == j else "red" for x in range(len(values))])
			    
			    time.sleep(0.1) 
			    return ( i+1 ) 
		
			def quickSort(arr,low,high):
				sortviz(arr,["blue" if x == low or x == high else "red" for x in range(len(values)) ])
				time.sleep(0.1)
				if (low < high):
					pi = partition(arr,low,high)
					quickSort(arr, low, pi-1)
					quickSort(arr, pi+1, high) 
			#sortviz(values)
			#time.sleep(0.2)
			quickSort(values,0,len(values)-1)
			sortviz(values,["green" for x in range(len(values))])
			time.sleep(0.1) 
			    
			print(values)
			
		elif x==4: #MERGE SORT
			def mergeSort(arr):
				#sortviz(values)
				#time.sleep(0.2)	 
				if len(arr) >1: 
					mid = len(arr)//2 # Finding the mid of the array 
					L = arr[:mid] # Dividing the array elements 
					R = arr[mid:] # into 2 halves 
					mergeSort(L) # Sorting the first half 
					mergeSort(R) # Sorting the second half 

					i = j = k = 0
					
					# Copy data to temp arrays L[] and R[] 
					while i < len(L) and j < len(R): 
			
						if L[i] < R[j]: 
							arr[k] = L[i] 
							i+= 1
							sortviz(values,["blue" if x == k or x == k+1 else "red" for x in range(len(values))])
							time.sleep(0.1)
			
						else: 
							arr[k] = R[j] 
							j+= 1
							sortviz(values,["green" if x == k or x == k+1 else "red" for x in range(len(values))])
							time.sleep(0.1)

						k+= 1
			
					while i < len(L): 
						arr[k] = L[i] 
						i+= 1
						k+= 1
						sortviz(values,["orange" if x == k or x == k+1 else "red" for x in range(len(values))])
						time.sleep(0.1)

					while j < len(R): 
						arr[k] = R[j] 
						j+= 1
						k+= 1
						sortviz(values,["yellow" if x == k or x == k+1 else "red" for x in range(len(values))])
						time.sleep(0.1)
					
				#sortviz(values,["green" for x in range(len(values))])
				#time.sleep(0.2)
			#calling function
			mergeSort(values)
			
			sortviz(values,["green" for x in range(len(values))])
			time.sleep(0.1)

					
			print(values)
		else:
			pass

def sortviz(value,color):
	canvas.delete("all")
	offset = 40
	spacing = 4
	width = (300/len(value))+1
	for i in range(0,len(value)):
		x1 = (i*width)+offset+spacing
		x2 = 400
		y1 = (i+1)*width + offset
		y2 = ((value[i]+1))*20
		
		canvas.create_rectangle(x1,x2,y1,y2,fill=color[i])
		canvas.create_text(x1+width/3,y2+(y2/3),text=max(value)-value[i]+1,fill="Black")
	
	root.update_idletasks()
	
	#print("after Sorting",value)


canvas.create_text(width/2,height/2,text="Sorting\nVisualization",font=("Algerian",40),fill="BLUE")
generateNew = Button(frame1,text="Generate Array",command=gen1,padx=100,pady=10,bg="orange",font=("Arial Black",10))
sort1 = Button(frame2,text="Bubble Sort",command=lambda:sort(1),pady=10,bg="orange",font=("Arial Black",10))
sort2 = Button(frame2,text="Selection Sort",command=lambda:sort(2),pady=10,bg="orange",font=("Arial Black",10))
sort3 = Button(frame2,text="Quick Sort",command=lambda:sort(3),pady=10,bg="orange",font=("Arial Black",10))
sort4 = Button(frame2,text="Merge Sort",command=lambda:sort(4),pady=10,bg="orange",font=("Arial Black",10))

generateNew.pack(padx=60,pady=10)
sort1.pack(side=LEFT,padx=5,pady=10)
sort2.pack(side=LEFT,padx=5,pady=10)
sort3.pack(side=LEFT,padx=5,pady=10)
sort4.pack(side=LEFT,padx=5,pady=10)
root.mainloop()