from tkinter import * 
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title' , 
                            'Monkeys can live upto 300 years') 

answer = tkinter.messagebox.askquestion('Question1'
                                        ,'Do you like me or not ' )
if(answer == 'yes') :
    print("Hey I also like you")
else : 
    print("Even I don't like you")
    

root.mainloop()
