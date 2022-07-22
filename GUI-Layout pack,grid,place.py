import tkinter as tk

pencere=tk.Tk()
pencere.geometry("500x500")
pencere.title("byKURT's screen")
pencere.configure(bg="pink")



etiket1=tk.Label(text="Etiket1",bg="blue",fg="yellow",font="Verdana 22")
etiket1.pack(side="left") #left, right, top, bottom

etiket2=tk.Label(text="Etiket2",bg="grey",fg="yellow",font="Verdana 22")
etiket2.pack(side="left")

etiket3=tk.Label(text="Etiket3",bg="red",fg="yellow",font="Verdana 22")
etiket3.pack(fill="x")   #x,y      #x ekseninde kalan alanı doldurur

etiket4=tk.Label(text="Etiket4",bg="green",fg="black",font="Verdana 22")
etiket4.pack(expand="yes") #yayılma yes,no



pencere.mainloop()

pencere2=tk.Tk()
pencere2.geometry("500x500")

p2e1=tk.Label(text="Etiket2",bg="grey",fg="yellow",font="Verdana 22")
p2e1.grid(row=0,column=0)

p2e2=tk.Label(text="Etiket4",bg="green",fg="black",font="Verdana 22")
p2e2.grid(row=1,column=1)

p2e3=tk.Label(text="Etiket5",bg="yellow",fg="black",font="Verdana 22")
p2e3.grid(row=1,column=2)

pencere2.mainloop()

pencere3=tk.Tk()
pencere3.geometry("500x500")

p3e1=tk.Label(text="Etiket2",bg="grey",fg="yellow",font="Verdana 22")
p3e1.place(x=20, y=20)

p3e2=tk.Label(text="Etiket2",bg="grey",fg="yellow",font="Verdana 22")
p3e2.place(x=200, y=150)




pencere3.mainloop()