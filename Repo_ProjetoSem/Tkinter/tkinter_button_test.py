from tkinter import *

root = Tk()

num = 0

def ctu():
    numero = Label(root, text='Mais')
    numero.pack()

def ctd():
    numero = Label(root, text='Menos')
    numero.pack()

btn1 = Button(root, text='+1', padx=50, pady=50, command=ctu)
btn1.pack()
btn2 = Button(root, text='-1', padx=50, pady=50, command=ctd)
btn2.pack()

root.mainloop()