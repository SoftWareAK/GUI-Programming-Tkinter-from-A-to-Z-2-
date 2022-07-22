import tkinter as tk
from tkinter import *

def choose():
    print(lb.curselection())
pencere=tk.Tk()


lb= Listbox(selectmode=MULTIPLE) #eğer buraya SINGLE YAZARSAM TEK SEÇİM YAPABİLİRİM
lb.insert(0,"Php")
lb.insert(1,"python")
lb.insert(2,"c++")
lb.insert(3,"java")
lb.place(x=10,y=10)

b=Button(text="Chooses",command=choose)
b.place(x=119,y=50)






pencere.mainloop()