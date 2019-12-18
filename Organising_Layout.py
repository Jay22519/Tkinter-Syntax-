from tkinter import * 

root = Tk()

one = Label(root ,  text = "one" , bg = "red" , fg ="white")  
one.pack() 

two = Label(root ,  text = "two" , bg = "blue" , fg ="white")  
two.pack(fill = X) 
#fill X means fill complete horizontal part , ie , cover complete row 

three = Label(root ,  text = "three" , bg = "yellow" , fg ="white") 
three.pack(side = LEFT,fill = Y)  



 
root.mainloop()
