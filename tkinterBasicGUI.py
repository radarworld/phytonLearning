from tkinter import *
from tkinter import Tk, Frame, Menu, messagebox, W, E, N, S
from tkinter.ttk import Separator, Style
from tkinter.scrolledtext import ScrolledText
import sys
import datetime
from radarControls import *

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

        topWindow.columnconfigure(0, weight=1)
        topWindow.columnconfigure(1, weight=1)
        topWindow.rowconfigure(0, weight=90)
        topWindow.rowconfigure(1, weight=3)
        topWindow.rowconfigure(2, weight=1)
        self.grid(sticky = W+E+N+S)
        

        self.master.title("Simple Demo")

        
        menubar = Menu(topWindow)
        topWindow.config(menu=menubar)
        
        fileMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open", command=MainWindow.doNothing)        
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=MainWindow.quit)

        editMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Settings", command=MainWindow.doNothing) 

        helpMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About", command=MainWindow.helpMenu_About)


        spaceHolder = Label(topWindow, text="radio buttons", bd=1, relief=SUNKEN, anchor=W)
        spaceHolder.grid(row=0, column=0)
                
        spaceHolder2 = Label(topWindow, text="graph", bd=4, relief=SUNKEN, anchor=W)
        spaceHolder2.grid(row=0, column=1, sticky = W+E+N+S)

        scrolled_text = ScrolledText(topWindow, state='disabled', height=5)
        scrolled_text.configure(font='TkFixedFont')
        scrolled_text.tag_config('INFO', foreground='black')
        scrolled_text.grid(row=1, column=0, columnspan=2, sticky = W+E+N+S)

        

        self.statusbarText=StringVar()
        self.statusBar = Label(topWindow, textvariable=self.statusbarText, bd=1, relief=SUNKEN, anchor=W)
        #self.statusBar.grid(row=2, column=0, columnspan=2, sticky = W+E+N+S)


        #sep = Separator(topWindow, orient="vertical")
        #sep.grid(row=0, column=1, sticky="ns")

        
    def helpMenu_About():
        messagebox.showinfo("About RadarWorld", "v0.0")
        
    def doNothing():
        pass
    
    def quit():
        root.destroy()

    def updateTime(self):     
        text=self.statusbarText.get()
        now = datetime.datetime.now()

        statusBarTextList=list()
        statusBarCurrentMsg="Version: RadarWorld 1.0"
        statusBarCurrentMsgExtended=statusBarCurrentMsg.ljust(len(statusBarCurrentMsg)+90)
        statusBarTextList.append(statusBarCurrentMsgExtended)
        
        statusBarCurrentState="Status: Connected via SER"
        statusBarCurrentMsgExtended=statusBarCurrentState.ljust(len(statusBarCurrentState)+70 )       
        statusBarTextList.append(statusBarCurrentMsgExtended)
                                                                
        statusBarCurrentTime=now.strftime("Time: %d-%m-%Y %H:%M:%S")        
        statusBarTextList.append(statusBarCurrentTime)
        
        self.statusbarText.set(''.join(statusBarTextList))
        
        self.statusBar.grid(row=2, column=0, columnspan=2, sticky = W+E+N+S)
        self.after(1000,self.updateTime)
        
        
        
        

#Tk is a class and it will be copied to the root variable. So Tk object can be referreed as root variable.        
#The command below also creates the root window.
#print (type(MainWindow))
root = Tk()
MainWindow(root).updateTime()


#Geometry manager Pack. Pack a widget in the parent widget with the grid() builder.
MainWindow(root).grid()

#tk.mainloop() blocks. What that means is that execution of your python program halts there
root.mainloop()



