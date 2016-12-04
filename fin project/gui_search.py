import Tkinter as tk
import Database as DB
import Widgets as wd

class gui_search:
    'App for creating a new student in the database'
    #################   CONSTRUCTOR   #################
    def __init__(self, db):
        '''
        Initialize a gui for the insertion of students infomation'
        INPUT: db - the databse
        '''
        #create a root container
        self.root = tk.Tk()
        self.root.title("awesome app")

        #Labels: to the left of the window
        search_label = wd.LabelWidget(self.root, 0, 0, "Search Past Records or Add New")
        search_label.grid(columnspan=4)
        search_label.config(width=30)

        #Entries: to the right of the window
        name_label = wd.LabelWidget(self.root, 0, 1, "Name")
        name_bar = wd.EntryWidget(self.root, 1, 1, "")
        name_bar.grid(columnspan=3)
        name_bar.config(width=20)

        #Topic
        topic_label = wd.LabelWidget(self.root, 0, 2, "Topic")
        topic_bar = wd.EntryWidget(self.root, 1, 2, "")
        topic_bar.grid(columnspan=3)
        topic_bar.config(width=20)

        #Date
        date_label = wd.LabelWidget(self.root, 0, 3, "Y-MM-DD")
        mm_bar = wd.EntryWidget(self.root, 2, 3, "")
        dd_bar = wd.EntryWidget(self.root, 3, 3, "")
        yy_bar = wd.EntryWidget(self.root, 1, 3, "")
        # dd_bar.grid(columnspan=1)
        # mm_bar.grid(columnspan=1)
        # yy_bard.grid(columnspan=1)
        mm_bar.config(width=4)
        dd_bar.config(width=4)
        yy_bar.config(width=7)

        #check button for the show
        show_var = tk.StringVar()
        show_checkbox = tk.Checkbutton(self.root, variable=show_var, onvalue="Yes", offvalue = "No")
        show_checkbox.deselect() #set the check button to offvalue
        show_checkbox.grid(column = 2, row=4)
        no_show_label = wd.LabelWidget(self.root, 0, 4, "No show")
        no_show_label.grid(columnspan=3)

        #Log display to the gui
        log = wd.LabelWidget(self.root, 0, 6, "Status")
        log.config(width = 30)
        #having the log display to span 2 columns
        log.grid(columnspan = 4)

        ## todo: reimplement
        def search_fn():
            'method to call for the search button'
            name_text = name_bar.getVal()
            topic_text = topic_bar.getVal()
            dd_text = dd_bar.getVal()
            mm_text = mm_bar.getVal()
            yy_text = yy_bar.getVal()
            try:
                #interaction with the Database object
                db.insVisit(idE.getVal(), dateE.getVal(), startE.getVal(), showVar.get(), TopicE.getVal(), noteE.getVal())
                #report that the insertion is success
                log.set("Success")
            except Exception, value:
                #If insertion fail, report to the Log display
                log.set(value)

        def add_fn():
            'method to call for the add button'
            name_text = name_bar.getVal()
            topic_text = topic_bar.getVal()
            dd_text = dd_bar.getVal()
            mm_text = mm_bar.getVal()
            yy_text = yy_bar.getVal()
            # TODO: IMPLEMENT ADD FUNCTION

        #A Submit button
        search_button = tk.Button(self.root, text="Search", command = search_fn)
        search_button.grid(column = 0, row=5, columnspan=2)

        add_button = tk.Button(self.root, text="Add", command = add_fn)
        add_button.grid(column = 2, row=5, columnspan=2)

        #make the window appears
        self.root.mainloop()



if __name__ == "__main__":
    #connecting with the database
    db = DB.Database('database/cup.db')
    new = gui_search(db)
