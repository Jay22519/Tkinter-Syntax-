from tkinter import * 

root = Tk()

label_1 = Label(root,text = "Name") 
label_2 = Label(root,text = "password")

entry_1 = Entry(root) 
entry_2 = Entry(root)
#Sticky = NEWS 
label_1.grid(row = 0 , column = 0 , sticky = E)
label_2.grid(row = 1 ,  column = 0, sticky = E) 

entry_1.grid(row = 0 , column = 1) 
entry_2.grid(row = 1 , column = 1 )


check = Checkbutton(root , text = "Keep me Logged In") 
check.grid(row = 2 , columnspan = 2 )


root.mainloop()
