from tkinter import *
root= Tk()


def myclick():
	mylabel = Label(root, text="I clicked the button!!")
	mylabel.pack()



#Creating buttons
mybutton1 = Button(root, text="Button" ,command=myclick, bg="#ffffff")


#Showingbutton
mybutton1.pack()


root.mainloop()


