from tkinter import *
root= Tk()
root.title("Calculator")



#Creating
e= Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
	current=e.get
	e.delete(0, END)
	e.insert(0, str(current) + str(number)


def buttonclear():
	e.delete(0, END)



# Buttons
mybutton1 = Button(root, text="1" , bg="white", padx=40, pady=20, command=lambda: button_click(1))
mybutton2 = Button(root, text="2" , bg="white", padx=40, pady=20, command=lambda: button_click(2))
mybutton3 = Button(root, text="3" , bg="white", padx=40, pady=20, command=lambda: button_click(3))
mybutton4 = Button(root, text="4" , bg="white", padx=40, pady=20, command=lambda: button_click(4))
mybutton5 = Button(root, text="5" , bg="white", padx=40, pady=20, command=lambda: button_click(5))
mybutton6 = Button(root, text="6" , bg="white", padx=40, pady=20, command=lambda: button_click(6))
mybutton7 = Button(root, text="7" , bg="white", padx=40, pady=20, command=lambda: button_click(7))
mybutton8 = Button(root, text="8" , bg="white", padx=40, pady=20, command=lambda: button_click(8))
mybutton9 = Button(root, text="9" , bg="white", padx=40, pady=20, command=lambda: button_click(9))
mybutton0 = Button(root, text="0" , bg="white" , padx=40, pady=20, command=lambda: button_click(0))
mybuttonadd = Button(root, text="+" , bg="white" , padx=40, pady=20, command=lambda: button_click())
mybuttonAC = Button(root, text="AC" , bg="white" , padx=83, pady=20, command=lambda: button_click())
mybuttonsub = Button(root, text="-" , bg="white" , padx=40, pady=22, command=lambda: button_click())
mybuttonmul = Button(root, text="*" , bg="white" , padx=40, pady=20, command=lambda: button_click())
mybuttondiv = Button(root, text="/" , bg="white" , padx=40, pady=20, command=lambda: button_click())

mybuttoneq = Button(root, text="=", bg="white" , padx=87, pady=20, command=button_click)


#Showing


mybutton1.grid(row=3, column=0)
mybutton2.grid(row=3, column=1)
mybutton3.grid(row=3, column=2)

mybutton4.grid(row=2, column=0)
mybutton5.grid(row=2, column=1)
mybutton6.grid(row=2, column=2)

mybutton7.grid(row=1, column=0)
mybutton8.grid(row=1, column=1)
mybutton9.grid(row=1, column=2)

mybutton0.grid(row=4, column=0)


mybuttonAC.grid(row=4, column=1, columnspan=2)

mybuttonadd.grid(row=5, column=0 )
mybuttonsub.grid(row=5, column=1 )
mybuttonmul.grid(row=5, column=2)
mybuttondiv.grid(row=6, column=0)
mybuttoneq.grid(row=6, column=1, columnspan=2, rowspan=1)




root.mainloop()
