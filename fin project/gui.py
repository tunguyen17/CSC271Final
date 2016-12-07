import Tkinter as tk
import Database as DB
import Widgets as wd

class NewVisit:
    'App for creating a new student in the database'
    #################   CONSTRUCTOR   #################
    def __init__(self, db):
        '''
        Test data
        '''

        try:
            data = db.findVisit("hawkeye20", "2015-04-22", "14:22")[0]
            stuName = ' '.join(db.findStudent("hawkeye20")[0][1:3])
        except IndexError:
            data = ["N/A" for i in range(1, 10)]
            stuName = "N/A"
        #create a root container
        self.root = tk.Tk()
        self.root.title("Visit's Comments")

        #upper part of the new comment Visit
        name = wd.LabelWidget(self.root, 0, 0, stuName)
        name.config(width = 20)
        #show no show
        showVar = tk.StringVar()
        showE = tk.Checkbutton(self.root, text= "Show/NoShow", variable=showVar, onvalue="Yes", offvalue = "No")

        if data[3].lower() == "yes":
            showE.select()
        else:
            showE.deselect() #set the check button to offvalue
        showE.grid(column = 1, row = 0)



        date = wd.LabelWidget(self.root, 0, 1, data[1])
        date.config(width = 20)
        time = wd.LabelWidget(self.root, 1, 1, data[2])
        time.config(width = 20)
        topic = wd.LabelWidget(self.root, 0, 2, data[4])
        topic.grid(columnspan = 2)
        topic.config(width = 50)


        #lower part of the new visit

        #new comments
        new = wd.LabelWidget(self.root, 0, 4, "NEW COMMENTS")
        new.grid(columnspan = 2)
        new.config(width = 50)
        newComments = wd.LabelWidget(self.root, 0, 5, "Student comments")
        newComments.config(width = 50)
        newComments.grid(columnspan = 2)
        comments = wd.TextWidget(self.root, 0, 6, 100, 10, "Insert Comments")
        comments.grid(columnspan = 2)

        #new observations
        newObservations = wd.LabelWidget(self.root, 0, 7, "Observations")
        newObservations.config(width = 50)
        newObservations.grid(columnspan = 2)
        observations = wd.TextWidget(self.root, 0, 8, 100, 10, "Insert Observations")
        observations.grid(columnspan = 2)

        #new recommendations
        newRecommendations = wd.LabelWidget(self.root, 0, 9, "Recommendations")
        newRecommendations.config(width = 50)
        newRecommendations.grid(columnspan = 2)
        recommendations = wd.TextWidget(self.root, 0, 10, 100, 10, "Insert Recommendations")
        recommendations.grid(columnspan = 2)

        #Log display to the gui
        log = wd.LabelWidget(self.root, 0, 12, "Status", 30)
        log.config(width = 50)
        #having the log display to span 2 columns
        log.grid(columnspan = 1)

        def ins():
            'method to call for the Submit button'
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
        submit.grid(column = 0, row=11, columnspan=2)

        #make the window appears
        self.root.mainloop()



if __name__ == "__main__":
    #connecting with the database
    db = DB.Database('database/cup.db')
    new = NewVisit(db)
