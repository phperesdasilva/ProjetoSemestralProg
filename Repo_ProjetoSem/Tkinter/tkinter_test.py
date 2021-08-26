from tkinter import *

root = Tk()
root.title('Tkinter Test')
root.geometry('400x400')

slposx = Scale(root, from_=0, to=100, orient=HORIZONTAL)
slposx.grid(row=0, column=0)

lbposx = Label(root, text=posx)
lbposx.grid(row=0, column=1)


btpos1 = Button(root, text='Pos. 1').grid(row=3, column=0)
btpos2 = Button(root, text='Pos. 2').grid(row=3, column=1)
btpos3 = Button(root, text='Pos. 3').grid(row=3, column=2)
btpos4 = Button(root, text='Pos. 4').grid(row=3, column=3)
btpos5 = Button(root, text='Pos. 5').grid(row=3, column=4)

root.mainloop()