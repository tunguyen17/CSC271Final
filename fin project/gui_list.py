import Tkinter as tk
import ttk
import Database as DB
import Widgets as wd

class GuiList:
    #################   CONSTRUCTOR   #################
    def __init__(self, top_lvl):

        #create container
        self.root = tk.Toplevel(top_lvl)
        self.root.title("Search results")

        ##set weight to the grid so that it can take up more space
        tk.Grid.rowconfigure(self.root, 0, weight=1)
        tk.Grid.columnconfigure(self.root, 0, weight=1)

    def draw_table(self, data):

        list_columns = [a[0] for a in data.description]

        ###  TREEVIEW INITIALIZATION AND CONFIGURATIONS  ###
        #create a tree view
        self.tree = ttk.Treeview(self.root, selectmode='extended')

        #Scrollbars
        self.ysb = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.xsb = ttk.Scrollbar(self.root, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)

        #make the table appears in grid
        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W,columnspan=8)
        self.ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.xsb.grid(row=1, column=0, sticky=tk.E + tk.W)

        ###  DATA  ###

        #index the column
        self.tree["columns"] = list_columns

        ## column name ##
        #columb attributes
        for i in list_columns:
            self.tree.column(i, minwidth=20)
            self.tree.heading(i, text=i)

        ##Actual data
        data = data.fetchall()
        index = 1

        for row in data:
            self.tree.insert('', 'end', text=str(index), values=(row))
            index+=1

        self.root.grab_set()

        #make the window appears
        # self.root.mainloop()

if __name__ == "__main__":
    gui = GuiList()

    #connecting with the database
    db = DB.Database('database/cup.db')

    gui.draw_table(db, 'visits')
