from tkinter import *
import time

def digital():
    d=time.strftime("%H:%M:%S")
    clock.config(text=d)
    clock.after(1,digital)
root=Tk()
root.title("DIGITAL clock")
clock=Label(root,font=("times",100,"bold"),bg="powderblue") 
clock.grid(row=2,column=1)
digital()
root.mainloop()    
