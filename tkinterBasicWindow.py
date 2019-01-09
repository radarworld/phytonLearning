import tkinter
import sys

'''This is an example of the tkinter class to learn the basics'''

#create MyWindow class inheriting from tk.Frame
class MyWindow(tkinter.Frame):
    
    #__init__ is called when ever an object of the class is constructed.
    def __init__(self, parent):

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
        tkinter.Frame.__init__(self, parent)
        
        label = tkinter.Label(self, text="Hello")
        label.pack()
        label.bind("<1>", self.quit)
    def quit(sel, event=None):
        sys.exit()
#Tk is a class and it will be copied to the root variable. So Tk object can be referreed as root variable.        
#The command below also creates the root window.
root = tkinter.Tk()

#Geometry manager Pack. Pack a widget in the parent widget.
MyWindow(root).pack()

#tk.mainloop() blocks. What that means is that execution of your python program halts there
root.mainloop()



