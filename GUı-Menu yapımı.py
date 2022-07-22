import tkinter as tk
from tkinter import *

def function():
    print("menu seçildi")


pencere=tk.Tk()

menucubugu=Menu(pencere)

file= Menu(menucubugu,tearoff=0)
file.add_command(label="New",command="function")
file.add_command(label="Open",command="function")
file.add_separator()   #araya çizgi çeker
file.add_command(label="Exit",command="fuction")

menucubugu.add_cascade(label="File",menu=file)


edit= Menu(menucubugu,tearoff=0)
edit.add_command(label="Cut",command="function")
edit.add_command(label="Copy",command="function")
edit.add_separator()   #araya çizgi çeker
edit.add_command(label="Paste",command="fuction")

menucubugu.add_cascade(label="Edit",menu=edit)





pencere.config(menu=menucubugu)
pencere.mainloop()