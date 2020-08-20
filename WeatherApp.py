# Author : Rohan Nirmal
# Here we need an api to read files from website.
# GO to any of the weather website and read the documentation.( Here i have used api from the website : Open Weather Map  )
# create an account an apply for free api.
#use your free api to read values related to weather
from tkinter import *
import requests
import json


root = Tk()
root.title("Weather App")
root.geometry("400x200")
root.iconbitmap("E:/python/gui/Weather.ico")
mylabel = Label(root, text=" Live Weather updates !",font=("Arial Black",15),bg="#ff4d4d",fg="white")
mylabel.pack()
frame1 = Frame(root,width=400,height=50)
frame1.config(bg="#537cf5")
frame1.pack(padx=10,pady=10)

frame2 = Frame(root,width=400,height=100)
frame2.config(bg="#4deb82")
frame2.pack(padx=10,pady=10)

frame3 = Frame(root,width=400,height=100)
frame3.config(bg="#4deb82")
frame3.pack(pady=2)
# show and update new values as new state selected
def show(c):
	selected_state = Label(frame2,text=str(c),font=("Lucida Console",13),fg="white",bg="black").grid(row=0,column=1)
	try:
		#city = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
		country = "ind"
		api = ''
		api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+c+","+country+"&APPID="##__YOUR__API__ID__##"")
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error"
	tem	= api["main"]["temp"] - 273.15
	print(tem)
	
	temp = Label(frame1, text=" Temperatue: " + str(int(api["main"]["temp"]- 273.15)),font=("Lucida Console",10),fg="white",bg="black").grid(row=0,column=0)
	pressure = Label(frame1, text=" Pressure: "+ str(api["main"]["pressure"]),font=("Lucida Console",10),fg="white",bg="black").grid(row=0,column=1)
	humidity = Label(frame1, text=" Humidity: " + str(api["main"]["humidity"]),font=("Lucida Console",10),fg="white",bg="black").grid(row=0,column=2)
	if tem >= 0 and tem<=10:
		color = "#3e49ed"
	if tem > 10 and tem <=20:
		color = "#3eedd9"
	if tem > 20 and tem <=30:
		color = "#a7ed3e"
	if tem >30 and tem<=40:
		color = "#f7e623"
	if tem >40:
		color = "#f54702"
	root.configure(background=color)


# by default the data for first state from list is displayed
try:
	city = ["Andhra Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Chandigarh","Daman","Delhi","Puducherry"]
	country = "ind"
	api = ''
	api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city[0]+","+country+"&APPID=1e444ba8b9ce8dfbeb54c045303027de")
	api = json.loads(api_request.content)
except Exception as e:
	api = "Error"

# defining and placing widegets
global variable 
variable = StringVar(root)
variable.set(city[0])
w =OptionMenu(frame2,variable,*city)
w.grid(row=0,column=0)


show_choice = Button(frame3,text="Show",fg="white",bg="black",pady=20,padx=40,font=("Lucida Console",12),command=lambda:show(variable.get())).pack()
tem	= api["main"]["temp"] - 273.15
print(tem)	

temp = Label(frame1,pady=1,text=" Temperature: " + str(int(api["main"]["temp"]- 273.15)),font=("Lucida Console",10),fg="white",bg="black")
pressure = Label(frame1, text=" Pressure: "+ str(api["main"]["pressure"]),font=("Lucida Console",10),fg="white",bg="black")
humidity = Label(frame1, text=" Humidity: " + str(api["main"]["humidity"]),font=("Lucida Console",10),fg="white",bg="black")
selected_state = Label(frame2,text=variable.get(),font=("Lucida Console",13),fg="white",bg="black")


temp.grid(row=0, column = 0)
pressure.grid(row=0,column=1)
humidity.grid(row=0,column=2)
selected_state.grid(row=0,column=1)

# color setting
def select_Color(tem):
	if tem >= 0 and tem<=10:
		color = "#3e49ed"
	if tem > 10 and tem <=20:
		color = "#3eedd9"
	if tem > 20 and tem <=30:
		color = "#a7ed3e"
	if tem >30 and tem<=40:
		color = "#f7e623"
	if tem >40:
		color = "#f54702"
	return color
root.configure(background=select_Color(tem))
root.mainloop()
