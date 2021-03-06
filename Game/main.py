from tkinter import *
import xmltodict
import time

with open("file.xml") as fd:
    doc = xmltodict.parse(fd.read())

root = Tk()
root.title("Student Life")
root.resizable(width=False, height=False)

mainWindow = Text(
    root,
    height=30,
    width=100,
    background = ('black'),
    foreground = ('white'),
    font = ('Courier',12),
    cursor = 'plus',
    state = 'disable',
)
mainWindow.pack(anchor = 'center', side = 'top')

def write(string):                                          #print stuff to screen as text
    mainWindow.config(state='normal')
    mainWindow.insert("end", "     " + string + "\n")
    mainWindow.see("end")
    mainWindow.config(state='disable')


console = Entry(root,
                width=100,
                background='#3D3D3D',
                foreground='white',
                #font=('Courier', 10),
                relief='flat',
                borderwidth=0,
                )
console.pack(anchor = 'center',
             #fill = 'both',
             side = 'bottom'
             )

console.insert(0,">>> ")