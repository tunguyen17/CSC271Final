from Tkinter import *

class safe: # the decorator
  def __init__(self, function):
    self.function = function

  def __call__(self, *args):
    try:
      return self.function(*args)
    except Exception, e:
      # make a popup here with your exception information.
      # might want to use traceback module to parse the exception info
      print "Error: %s" % (e)

@safe
def bad():
    1/0

root = Tk()
b = Button(root, text="press me", command=bad)
b.pack()
