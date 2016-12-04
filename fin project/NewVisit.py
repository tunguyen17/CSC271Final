import Tkinter as tk
import Database as DB
import Widgets as wd

class NewVisit:
    'App for creating a new student in the database'
    #################   CONSTRUCTOR   #################
    def __init__(self, db):
        '''
        Initialize a gui for the insertion of students infomation'
        INPUT: db - the databse
        '''
        #create a root container
        self.root = tk.Tk()
        self.root.title("New Visit")

        #Labels: to the left of the window
        idL = wd.LabelWidget(self.root, 0, 0, "ID")
        dateL = wd.LabelWidget(self.root, 0, 1, "Visit Date")
        startL = wd.LabelWidget(self.root, 0, 2, "Visit Start")
        showL = wd.LabelWidget(self.root, 0, 3, "Show")
        topicL = wd.LabelWidget(self.root, 0, 4, "Topic")
        noteL = wd.LabelWidget(self.root, 0, 5, "Note")
        noteL.grid(columnspan=2)


        #Entries: to the right of the window
        idE = wd.EntryWidget(self.root, 1, 0, "ID")
        dateE = wd.EntryWidget(self.root, 1, 1, "YYYY-MM-DD")
        startE = wd.EntryWidget(self.root, 1, 2, "HH:MM")
        #check button for the show
        showVar = tk.StringVar()
        showE = tk.Checkbutton(self.root, variable=showVar, onvalue="Yes", offvalue = "No")
        showE.deselect() #set the check button to offvalue
        showE.grid(column = 1, row=3)
        TopicE = wd.EntryWidget(self.root, 1, 4, "Topic")
        TopicE.config(width = 50)
        noteE = wd.TextWidget(self.root, 0, 6, 100, 10, "Insert Note")
        noteE.grid(columnspan = 2)

        #Log display to the gui
        log = wd.LabelWidget(self.root, 0, 8, "Status", 30)
        log.config(width = 80)
        #having the log display to span 2 columns
        log.grid(columnspan = 2)

        def ins():
            'method to call for the Submit button'
            if idE.getVal() not in db.idList():
                log.set("ID not found. Please insert student first!")
            else:
                try:
                    #interaction witht the Database object
                    db.insVisit(idE.getVal(), dateE.getVal(), startE.getVal(), showVar.get(), TopicE.getVal(), noteE.getVal())
                    #report that the insertion is success
                    log.set("Success")
                except Exception, value:
                    #If insertion fail, report to the Log display
                    log.set(value)

        #A Submit button
        submit = tk.Button(self.root, text="Submit", command = ins)
        submit.grid(column = 0, row=7, columnspan=2)

        #make the window appears
        self.root.mainloop()



if __name__ == "__main__":
    #connecting with the database
    db = DB.Database('database/cup.db')
    new = NewVisit(db)
