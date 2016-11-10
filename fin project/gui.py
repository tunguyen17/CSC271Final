import Tkinter as tk
import ttk

class Gui:
    #################   CONSTRUCTOR   #################
    def __init__(self, master):
        
        list_columns = ["ID", "First", "Last", "Year"]
        #create a tree view
        self.tree = ttk.Treeview(master)
        #index the column
        self.tree["columns"] = list_columns

        self.tree.column("#0", width=50)
        self.tree.heading("#0", text="No.")

        for i in list_columns:
            self.tree.column(i, width=100 )
            self.tree.heading(i, text=i)


        #Scrollbars
        self.ysb = ttk.Scrollbar(root, orient='vertical', command=self.tree.yview)
        self.xsb = ttk.Scrollbar(root, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)


        #make the table appears in grid
        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W,columnspan=8)
        self.ysb.grid(row=1, column=9, sticky=tk.N + tk.S + tk.E + tk.W)
        self.xsb.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, columnspan=8)

if __name__ == "__main__":
    #Initialize a Tk root widget
    root = tk.Tk()
    #set weight to the grid so that it can take up more space
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)

    gui = Gui(root)

    #make the window appears
    root.mainloop()
