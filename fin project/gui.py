import Tkinter as tk
import ttk
import Database as DB

class Gui:
    #################   CONSTRUCTOR   #################
    def __init__(self):

        #create container
        self.root = tk.Tk()

        ##set weight to the grid so that it can take up more space
        tk.Grid.rowconfigure(self.root, 0, weight=1)
        tk.Grid.columnconfigure(self.root, 0, weight=1)

    def draw_table(self, db, r):

        list_columns = [a[1] for a in db.meta[r]]

        ###  TREEVIEW INITIALIZATION AND CONFIGURATIONS  ###
        #create a tree view
        self.tree = ttk.Treeview(self.root)

        #Scrollbars
        self.ysb = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.xsb = ttk.Scrollbar(self.root, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)

        #make the table appears in grid
        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W,columnspan=8)
        self.ysb.grid(row=1, column=9, sticky=tk.N + tk.S + tk.E + tk.W)
        self.xsb.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, columnspan=8)

        ###  DATA  ###

        #index the column
        self.tree["columns"] = list_columns

        ## column name ##
        #row ndex
        self.tree.column("#0", width=50)
        self.tree.heading("#0", text="No.")
        #columb attributes
        for i in list_columns:
            self.tree.column(i, width=100 )
            self.tree.heading(i, text=i)





        #make the window appears
        self.root.mainloop()

if __name__ == "__main__":
    #gui = Gui()

    #connecting with the database
    db = DB.Database('database/cup.db')

    #gui.draw_table(db, 'students')

    print db.fetchData('students')
