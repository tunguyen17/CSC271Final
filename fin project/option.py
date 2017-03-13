from Tkinter import *
import Database as DB
# the constructor syntax is:
# OptionMenu(master, variable, *values)


db = DB.Database('cup.db')

OPTIONS = [i[0] for i in db.getTopics()]
master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = apply(OptionMenu, (master, variable) + tuple(OPTIONS))
w.pack()

mainloop()
