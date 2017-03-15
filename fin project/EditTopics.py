import Tkinter as tk
import Database as DB
import Widgets as wd

class EditTopics:
    'App for creating a new student in the database'
    #################   CONSTRUCTOR   #################
    def __init__(self, top_lvl, db, master_topic):
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
        self.master_tp = master_topic
        #Labels: to the left of the window
        TopicLNew = wd.LabelWidget(self.root, 0, 0, "New Topic")
        TopicLNew.config(width = 12)
        TopicLRemove = wd.LabelWidget(self.root, 0, 1, "Remove Topic")
        TopicLRemove.config(width = 12)

        #Entries: to the right of the window
        TopicE = wd.EntryWidget(self.root, 1, 0, "")
        TopicE.config(width = 50)

        OPTIONS = [i[0] for i in db.getTopics()]
        TopicR = wd.OptionsWidget(self.root, OPTIONS ,1, 1)
        TopicR.config(width = 50)

        # firstE = wd.EntryWidget(self.root, 1, 1, "")

        #Log display to the gui
        log = wd.LabelWidget(self.root, 0, 7, "Status", 30)
        #having the log display to span 2 columns
        log.grid(columnspan = 2)

        # def refresh():
        #     OPTIONS = [i[0] for i in db.getTopics()]
        #     TopicR = wd.OptionsWidget(self.root, OPTIONS ,1, 1)
        #     TopicR.config(width = 50)


        def ins():
            'method to call for the Submit button'
            try:
                #checking if the user had inserted any special note for each students
                #interaction witht the Database object
                OPTIONS = [i[0] for i in db.getTopics()]
                newval = TopicE.getVal()
                if newval == "":
                    log.set("New Topic is empty")
                elif newval in OPTIONS:
                    log.set("Topic duplicated")
                else:
                    db.insTopic(newval)
                    OPTIONS = [i[0] for i in db.getTopics()]
                    TopicR.update_option_menu(OPTIONS)
                    self.master_tp.update_option_menu(OPTIONS)
                    #report that the insertion is success
                    log.set("Success")
            except Exception, value:
                #If insertion fail, report to the Log display
                log.set(value)

        def remove():
            try:
                #checking if the user had inserted any special note for each students
                #interaction witht the Database object
                val = TopicR.getVal()
                if val == "":
                    log.set("Can't delete null topic")
                # print TopicR["menu"]
                else:
                    db.delTopic(TopicR.getVal())
                    OPTIONS = [i[0] for i in db.getTopics()]
                    TopicR.update_option_menu(OPTIONS)
                    self.master_tp.update_option_menu(OPTIONS)
                    #report that the insertion is success
                    log.set("Success")
            except Exception, value:
                #If insertion fail, report to the Log display
                log.set(value)

        #Add button
        add = tk.Button(self.root, text="Add Topic", command = ins)
        add.grid(column = 3, row=0, columnspan = 2)

        #Add button
        remv = tk.Button(self.root, text="Remove Topic", command = remove)
        remv.grid(column = 3, row=1, columnspan = 2)

        self.root.grab_set()

        #make the window appears
        self.root.mainloop()


if __name__ == "__main__":
    #connecting with the database
    root = tk.Tk()
    db = DB.Database('cup.db')
    new = EditTopics(root,db)
