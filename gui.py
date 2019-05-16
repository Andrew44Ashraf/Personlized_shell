from tkinter import *
from tkinter import scrolledtext
import os

window= Tk()
window.title("Shell")

window.geometry('350x200')
 
 
txt = scrolledtext.ScrolledText(window,width=150,height=150)
 
txt.grid(column=0,row=0)


def keydown(e):
 
    #print(e.char)
    i = txt.count(0.0,1000000.0,"displaylines")
    x = txt.get(float(i[0]),10000000.0)
    x= x.split('\n')[0]
    #x= x.split(':')[1]
    if(x.split()[0] == 'cd'):
        try:
            x.split()[1]
            os.chdir(x.split()[1])
        except:
            txt.insert("insert","\nEnter directory")
    txt.insert("insert","\n\""+os.getcwd()+"\":  ")
    txt.delete("insert", "insert -1 chars")
 
#btn = Button(window, text="Click Me", command=clicked)
 
#btn.grid(column=1, row=0)
txt.bind('<Return>', keydown)
txt.insert(0.0,"\""+os.getcwd()+"\": \n")
window.mainloop()

