from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.filename = tkFileDialog.asksaveasfilename()
print (root.filename)
