from tkinter import *  
class Tkinter : 
    def __init__(self, master) : 
        frame = Frame(master)
        frame.pack() 
        
        self.printButton = Button(frame , 
                        text = "Print message" , 
                                  command = self.printMessage)
        self.printButton.pack(side = LEFT) 
        
        self.quitButton = Button(frame , 
                        text = "Quit" , 
                                  command = frame.quit)
        self.quitButton.pack(side = LEFT ) 
        
        
    def printMessage(self) : 
        print("Hey there My name is Jay , what's your ??") 
root = Tk()
b = Tkinter(root)

root.mainloop() 
