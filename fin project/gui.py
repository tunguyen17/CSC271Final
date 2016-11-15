import Tkinter as tk
import ttk
import Database as DB
import Widgets as wd
import sys

class Gui:
    #################   CONSTRUCTOR   #################
    def __init__(self):

        #create container
        self.root = tk.Tk()


    def studentIns(self, db):

        idL = wd.LabelWidget(self.root, 0, 0, "Name")
        firstL = wd.LabelWidget(self.root, 0, 1, "First")
        lastL = wd.LabelWidget(self.root, 0, 2, "Last")
        yearL = wd.LabelWidget(self.root, 0, 3, "Year")

        log = wd.LabelWidget(self.root, 0, 5, "Status", 30)

        idE = wd.EntryWidget(self.root, 1, 0, "ID")
        firstE = wd.EntryWidget(self.root, 1, 1, "First")
        lastE = wd.EntryWidget(self.root, 1, 2, "Last")
        yearE = wd.EntryWidget(self.root, 1, 3, "Year")

        def ins():
            try:
                db.insStudent(idE.getVal(), firstE.getVal(), lastE.getVal(), int(yearE.getVal()))
                log.set("Success")
            except Exception, value:
                log.set(value)

        submit = tk.Button(self.root, text="Submit", command = ins)
        submit.grid(column = 1, row=4)

        #make the window appears
        self.root.mainloop()

if __name__ == "__main__":
    gui = Gui()

    #connecting with the database
    db = DB.Database('database/cup.db')

    gui.studentIns(db)
