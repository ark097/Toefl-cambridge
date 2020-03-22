# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:25:55 2020

@author: aho9kor
"""
from tkinter import * 
from tkinter import messagebox
import os
working_dir = os.getcwd()

def goto(linenum):
    global line
    line = linenum
            
window = Tk()
window.title('File comparer')
window.minsize(640,400)

l1 = Label(window,text='Enter filename to search',font='none 10 bold')
l1.grid(row=0,column=0,sticky=W)

Search_Bar = Entry(window,width=50)
Search_Bar.grid(row=1,column=0,sticky=W)

Output_box = Text(window,width=100)
Output_box.grid(row=3,column=0,sticky=W)

def hey():
    for subdir, dirs, files in os.walk(working_dir):
        for file in files:
            filepath = subdir + os.sep + file
#            if Search_Bar.get() not in filepath:
#                messagebox.showinfo('ERROR','File not found!')
#                if messagebox.OK:
#                    window.mainloop()
            if Search_Bar.get() in filepath:
                #Output_box.delete('1.0',END)
                Output_box.insert(END,'\t     '+filepath+"\nSearch again:\t")
            else:
                messagebox.showinfo('ERROR','File not found!')
                if messagebox.OK:
                    goto(47)

Submit_button = Button(window, text="Search", width=10,command=hey)
Submit_button.grid(row=2, column=0)

window.mainloop()







