#!/usr/bin/env python
import Tkinter as tk
import ttk
import Database as DB
import Widgets as wd
import sqlite3
import EditVisit as ev
import NewVisit as nv

class StudentList:
    'App for creating a new student in the database'
    #################   CONSTRUCTOR   #################
    def __init__(self, db, top_lvl, student_data, data):
        '''
        Initialize a gui for the insertion of students infomation'
        INPUT: db - the databse
        '''

        self.id_no = student_data[0]
        self.id_name = student_data[1]
        self.id_cmt = student_data[2]

        #create a root container
        self.top_lvl = top_lvl
        self.root = tk.Toplevel(top_lvl)
        self.root.title(self.id_name)

        #upper parts : display crucial infomation

        #Labels: to the left of the window
        dateL = wd.LabelWidget(self.root, 1, 0, self.id_name,50)
        startL = wd.LabelWidget(self.root, 0, 0, self.id_no,25)



        #lower part, display long text
        #Visit NOTE
        noteL = wd.LabelWidget(self.root, 0, 1, "Student Note",25)
        noteL.grid(columnspan=4)
        noteE = wd.TextWidget(self.root, 0, 2, 127, 10, self.id_cmt)
        noteE.grid(columnspan=2)
        oldNote = noteE.getVal() #store the old note for comparision later


        #Log display to the gui
        log = wd.LabelWidget(self.root, 0, 100, "Status", 30)
        log.config(width = 100)
        #having the log display to span 2 columns
        log.grid(columnspan = 3)

        ### CLONED FROM TREEVIEW
        list_columns = [a[0] for a in data.description]
        ###  TREEVIEW INITIALIZATION AND CONFIGURATIONS  ###
        #create a tree view
        self.tree = ttk.Treeview(self.root, selectmode='browse')

        #Scrollbars
        self.ysb = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.xsb = ttk.Scrollbar(self.root, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)

        #make the table appears in grid
        self.tree.grid(row=10, column=0, sticky=tk.N + tk.S + tk.E + tk.W, columnspan=3)
        self.ysb.grid(row=10, column=4, sticky=tk.N + tk.S)
        self.xsb.grid(row=11, column=0, sticky=tk.E + tk.W, columnspan=3)

        def onDoubleClick(event):
            item = self.tree.identify('item', event.x, event.y)
            values = self.tree.item(item, "values")
            date_field = values[0]
            time_field = values[1]
            self.root.destroy()
            ev.EditVisit(db, self.top_lvl, self.id_no, date_field, time_field)

        self.tree.bind("<Double-1>", onDoubleClick)

        ###  DATA  ###
        columns=list_columns
        #index the column
        self.tree["columns"] = columns

        ## column name ##
        #row ndex
        self.tree.column("#0", width=100, anchor=tk.W)
        self.tree.heading("#0", text="No.")
        #column attributes
        self.tree["displaycolumns"] = list_columns
        for i in list_columns:
            self.tree.column(i, minwidth=20)
            self.tree.heading(i, text=i)

        ##Actual data
        data = data.fetchall()
        index = 1

        for row in data:
            self.tree.insert('', 'end', text=str(index), values=(row))
            index+=1

        def update_fn():
            'method to call for the Submit button'
            try:
                #interaction witht the Database object
                db.insVisit(idE.getVal(), dateE.getVal(), startE.getVal(), showVar.get(), TopicE.getVal(), nt, comm, obs, rec)
                #report that the insertion is success
                log.set("Success")
            except Exception, value:
                #If insertion fail, report to the Log display
                log.set(value)

        #A Submit button
        note_update = tk.Button(self.root, text="Update student", command = update_fn)
        note_update.grid(column = 0, row=9)

        def new_fn():
            self.root.destroy()
            nv.NewVisit(db, top_lvl, self.id_no)

        #A Submit button
        new_button = tk.Button(self.root, text="New visit", command = new_fn)
        new_button.grid(column = 1, row=9)

        self.root.grab_set()

        #make the window appears
        # self.root.mainloop()



if __name__ == "__main__":
    #connecting with the database
    db = DB.Database('database/cup.db')
    ID='hawkeye20'
    con = sqlite3.connect('database/cup.db')
    cur = con.cursor()
    data =cur.execute('select * from visits where ID=?',[ID])
    new = StudentList(tk.Tk(), ['',''], data)
