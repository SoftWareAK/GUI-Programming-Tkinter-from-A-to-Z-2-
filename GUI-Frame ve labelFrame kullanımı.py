import tkinter as tk
from tkinter import *


pencere=tk.Tk()
pencere.geometry("500x500")

fred=Frame(bg="RED",width=300,height=150)
fred.place(x=10,y=10)
b1=Button(fred,text="Kırmızı Frame butonu")
b1.place(x=10,y=10)

fblue=Frame(bg="BLUE",width=300,height=150)
fblue.place(x=150,y=170)
b2=Button(fblue,text="Mavi Frame butonu")
b2.place(x=10,y=10)

lb=LabelFrame(text="Etiketli Frame",width=200,height=150)
lb.place(x=50,y=330)
b3=Button(lb,text="Etiketli  Frame butonu")
b3.place(x=10,y=10)

pencere.mainloop()