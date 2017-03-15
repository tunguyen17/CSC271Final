import Tkinter as tk
import Database as DB
import Widgets as wd
import tkFileDialog

class Export_CSV:
    'App for creating a new student in the database'
    #################   CONSTRUCTOR   #################
    def __init__(self, top_lvl, db):
        '''
        Initialize a gui for the insertion of students infomation'
        INPUT:
            - top_lvl the top_lvl window
            -db - the databse
        '''
        #create a root container
        self.root = tk.Toplevel(top_lvl)
        self.root.title("Edit Topics")
        self.top_lvl = top_lvl

        #Log display to the gui
        log = wd.LabelWidget(self.root, 0, 7, "Status", 30)
        #having the log display to span 2 columns
        log.grid(columnspan = 4)


        def exportDB():
            'method to call for the Submit button'
            try:
                csv_directory = tkFileDialog.asksaveasfilename()
                db.export_csv(csv_directory)
                log.set("Exported:" + csv_directory)
            except Exception, value:
                #If insertion fail, report to the Log display
                log.set(value)

        def resetDB():
            try:
                #checking if the user had inserted any special note for each students
                #interaction witht the Database object
                db.resetDB()
                log.set("DB reseted")
            except Exception, value:
                #If insertion fail, report to the Log display
                log.set(value)

        #Add button
        add = tk.Button(self.root, text="Export CSV", command = exportDB)
        add.grid(column = 0, row=1, columnspan = 2)

        #Add button
        remv = tk.Button(self.root, text="Reset Database", command = resetDB)
        remv.grid(column = 2, row=1, columnspan = 2)

        self.root.grab_set()

        #make the window appears
        self.root.mainloop()


if __name__ == "__main__":
    #connecting with the database
    root = tk.Tk()
    db = DB.Database('cup.db')
    # new = EditTopics(root,db)
