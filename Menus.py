from tkinter import * 

def Menus() :
    print("This is my menu ..." ) 


root = Tk()

menu1 = Menu(root)
root.config(menu = menu1)

submenu = Menu(menu1)  
menu1.add_cascade(label = "File" , menu = submenu)  

submenu.add_command(label = "New Project" , command = Menus) 

submenu.add_separator() 

editMenu = Menu(menu1) 
menu1.add_cascade(label = "Edit" , menu = editMenu) 

editMenu.add_command(label = "New Project" , command = Menus) 

editMenu.add_separator() 



root.mainloop()
