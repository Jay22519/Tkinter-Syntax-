from tkinter import * 

root = Tk()  

canvas = Canvas(root,  width = 200 , height = 200) 
canvas.pack()

blackLine = canvas.create_line(0,0,250,50) #X and Y are 0,0 and ending 250 , 50
redLine = canvas.create_line(0,100,250,50, fill = "red" )  

greenBox = canvas.create_rectangle(25,25,130,60, fil = "green")
#Top left point (First 2 para)
# Next two are width and height

canvas.delete(redLine)
#It will delete redLine

#To delete all the diagrams of canvas -> 
canvas.delete(ALL)

root.mainloop()
