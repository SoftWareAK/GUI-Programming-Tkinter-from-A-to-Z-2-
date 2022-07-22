import tkinter as tk
from tkinter import *


window=tk.Tk()

pw1=PanedWindow(bg="RED",width=200,height=150)
pw1.place(x=0,y=0)

l1=Label(pw1,text="Red's Pane")
l1.place(x=10,y=10)


pw2=PanedWindow(bg="blue",width=100,height=100)
pw2.place(x=50,y=50)

l2=Label(pw2,text="Blue's Pane")
l2.place(x=10,y=10)


window.mainloop()