from tkinter import *
from tkinter import Tk, Frame, Menu, messagebox
from tkinter.scrolledtext import ScrolledText
import sys

'''This is an example of the tkinter class to learn the basics'''

#create MyWindow class inheriting from tk.Frame
class MainWindow(Frame):
    
    #__init__ is called when ever an object of the class is constructed.
    def __init__(self, topWindow):

        #these are not functions, even though they act just like functions.
        #They are actually called "methods." __init__ is a very special
        #method, in that this method always runs. Init is short of initialize,
        #and whatever you put in here is going to always run whenever the class
        #is called upon. The other methods will only run when you specifically
        #call upon them to run.
        
        #subclassing (inheriting from) the Tkinter class Frame.This means
        #instances of your class are also instances of Frame, and can be
        #used like Frames, and can use the internal behavior of Frame.

        #parent represents a widget to act as the parent of the current
        #object. All widgets in tkinter except the root window require a
        #parent (sometimes also called a master)
        Frame.__init__(self, topWindow)
        self.master  = topWindow

        #set topWindow to XGA+ resolution
        topWindow.geometry('%dx%d' % (1152, 864))
        topWindow.minsize(1152,864)
        #label = tkinter.Label(self, text="Hello")
        #label.pack()
        #label.bind("<1>", self.quit)

        self.master.title("Simple Demo")

        
        menubar = Menu(topWindow)
        topWindow.config(menu=menubar)
        
        fileMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open", command=MainWindow.doNothing)        
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=MainWindow.doNothing)

        editMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Settings", command=MainWindow.doNothing) 

        helpMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About", command=MainWindow.helpMenu_About)

        scrolled_text = ScrolledText(topWindow, state='disabled', height=5)
        scrolled_text.configure(font='TkFixedFont')
        scrolled_text.tag_config('INFO', foreground='black')


        spaceHolder = Label(topWindow, text="radio buttons", bd=1, relief=SUNKEN, anchor=W)
        spaceHolder.grid(row=0, column=0)


        spaceHolder2 = Label(topWindow, text="graph", bd=1, relief=SUNKEN, anchor=E)
        spaceHolder2.grid(row=0, column=1)

        

        statusBar = Label(topWindow, text="status bar...", bd=1, relief=SUNKEN, anchor=W)
        statusBar.grid(row=1, column=0, columnspan=1)

        



        
    def helpMenu_About():
        messagebox.showinfo("About RadarWorld", "v0.0")
        
    def doNothing():
        pass
    
    def quit(sel, event=None):
        sys.exit()
#Tk is a class and it will be copied to the root variable. So Tk object can be referreed as root variable.        
#The command below also creates the root window.
root = Tk()

#Geometry manager Pack. Pack a widget in the parent widget with the grid() builder.
MainWindow(root).grid()

#tk.mainloop() blocks. What that means is that execution of your python program halts there
root.mainloop()



