from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root = Tk()
root.geometry("500x500")
root.title("Project 171")
australia_img = ImageTk.PhotoImage(Image.open("australia.jpg"))
japan_img = ImageTk.PhotoImage(Image.open("japan.jpg"))
india_img = ImageTk.PhotoImage(Image.open("india.jpg"))
usa_img = ImageTk.PhotoImage(Image.open("usa.jpg"))

australia_label = Label(root, text = "Australia")
australia_map = Label(root, image = australia_img)
australia_time = Label(root)
australia_label.place(relx = 0.3, rely = 0.1, anchor = CENTER)
australia_map.place(relx = 0.3, rely = 0.3, anchor = CENTER)
australia_time.place(relx = 0.3, rely = 0.5, anchor = CENTER)

japan_label = Label(root, text = "Japan")
japan_map = Label(root, image = japan_img)
japan_time = Label(root)
japan_label.place(relx = 0.7, rely = 0.1, anchor = CENTER)
japan_map.place(relx = 0.7, rely = 0.3, anchor = CENTER)
japan_time.place(relx = 0.7, rely = 0.5, anchor = CENTER)

india_label = Label(root, text = "India")
india_map = Label(root, image = india_img)
india_time = Label(root)
india_label.place(relx = 0.3, rely = 0.6, anchor = CENTER)
india_map.place(relx = 0.3, rely = 0.8, anchor = CENTER)
india_time.place(relx = 0.3, rely = 0.9, anchor = CENTER)

usa_label = Label(root, text = "US")
usa_map = Label(root, image = usa_img)
usa_time = Label(root)
usa_label.place(relx = 0.7, rely = 0.6, anchor = CENTER)
usa_map.place(relx = 0.7, rely = 0.8, anchor = CENTER)
usa_time.place(relx = 0.7, rely = 0.9, anchor = CENTER)

class Australia() :
    def times(self) :
        home = pytz.timezone('Australia/ACT')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        australia_time["text"] = current_time
        
class Japan() :
    def times(self) :
        home = pytz.timezone('Japan')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        japan_time["text"] = current_time
        
class India() :
    def times(self) :
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = current_time
        
class Usa() :
    def times(self) :
        home = pytz.timezone('US/Eastern')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time["text"] = current_time

obj1 = Australia()
obj2 = Japan()
obj3 = India()
obj4 = Usa()
btn1 = Button(root, text = "Time", command = obj1.times)
btn2 = Button(root, text = "Time", command = obj2.times)
btn3 = Button(root, text = "Time", command = obj3.times)
btn4 = Button(root, text = "Time", command = obj4.times)
btn1.place(relx = 0.3, rely = 0.2, anchor = CENTER)
btn2.place(relx = 0.7, rely = 0.2, anchor = CENTER)
btn3.place(relx = 0.3, rely = 0.7, anchor = CENTER)
btn4.place(relx = 0.7, rely = 0.7, anchor = CENTER)
root.mainloop()