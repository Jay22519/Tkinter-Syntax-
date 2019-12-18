from tkinter import * 

def Menus() :
    print("This is my menu ..." ) 

root = Tk()
toolbar = Frame(root , bg = "blue")   
insertButt = Button(toolbar , text = "Insert Image" , command = Menus) 
insertButt.pack(side = LEFT , padx = 2 , pady = 4) 
printButt = Button(toolbar , text = "Print" , command = Menus) 
insertButt.pack(side = LEFT , padx = 4 , pady = 3)   

toolbar.pack(side = TOP , fill = X) 

root.mainloop()
