from tkinter import * 

root = Tk()

topframe = Frame(root) 
topframe.pack() 

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)   

button1 = Button(topframe , text = "Hey Top Frame" , fg ="red")
button2 = Button(topframe , text = "Hey Top Frame1" , fg ="yellow")
button3 = Button(topframe , text = "Hey Top Frame2" , fg ="green")
button4 = Button(bottomframe , text = "Hey Bottom Frame" , 
                 fg ="blue")  

button1.pack()
button2.pack()
button3.pack()
button4.pack()






root.mainloop()

