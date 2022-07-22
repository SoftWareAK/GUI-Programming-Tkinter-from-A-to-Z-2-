import tkinter as tk
from tkinter import *

from tkinter import messagebox

def goster():
    messagebox.showinfo("Mesajınız burada gösterilecek","Hosgeldiniz")
    mesaj.set("Bu da pencereden sonraki mesaj")
    m.place(x=75,y=100)

pencere=tk.Tk()

mesaj=StringVar()
m=Message(textvariable=mesaj,relief=RAISED)

b=Button(text="mesaj göster",command=goster)
b.place(x=20,y=20)



pencere.mainloop()