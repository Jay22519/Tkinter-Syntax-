
#Sorry for the mistake , but some part of grid is covered in Fitting Widgets

from tkinter import * 

root = Tk()

def printname() :
    print("Hello my name is Jay !!!  what's your") 

def printnamevent(event) :
    print("Hello my name is Jay !!!  what's your") 
    
button1 = Button(root, text = "PrintName" , command = printname) 
button1.grid(row = 0 ,  column = 0 ) 

button2 = Button(root, text = "PrintName" , command = printname) 
button2.bind("<Button-1>" , printnamevent ) 



root.mainloop()

