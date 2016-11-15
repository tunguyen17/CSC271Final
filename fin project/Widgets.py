import Tkinter as tk

#selectable grid for the label
class LabelWidget(tk.Entry):
    def __init__(self, master, x, y, text):
        self.text = tk.StringVar()
        self.text.set(text)
        tk.Entry.__init__(self, master=master)
        self.config(textvariable=self.text, width=8,
                    relief="ridge",
                    bg="#ffffff000", fg="#000000fff",
                    readonlybackground="#ffffff000",
                    justify='center',
                    state="readonly") #state = read only
        self.grid(column=x, row=y)

        #enable select_all
        self.bind("<Command-Key-a>", self.select_all)
        self.bind("<Command-Key-A>", self.select_all) # just in case caps lock is on

    def select_all(self, event):
        self.select_range(0, tk.END)
        self.icursor(tk.END) #bring the crusor to the end
        self.xview(tk.END) #bring the view to the end


#entry grid for something
class EntryWidget(tk.Entry):
    def __init__(self, master, x, y, text=""):
        tk.Entry.__init__(self, master=master)
        self.value = tk.StringVar()
        self.value.set(text)
        self.config(textvariable=self.value, width=8,
                    relief="ridge",
                    bg="#ddddddddd", fg="#000000000",
                    justify='center')
        self.grid(column=x, row=y)

        #enable select_all
        self.bind("<Command-Key-a>", self.select_all)
        self.bind("<Command-Key-A>", self.select_all) # just in case caps lock is on
    def getVal(self):
        return self.value.get()

    def select_all(self, event):
        self.select_range(0, tk.END)
        self.icursor(tk.END) #bring the crusor to the end
        self.xview(tk.END) #bring the view to the end

class TextWidget(tk.Text):
    def __init__(self, master, x, y, w, h, text = ""):
        tk.Text.__init__(self, master=master, width = w, height = h)
        #insert the default value
        self.insert(1.0, text)
        self.grid(column = x, row = y)
        sb = tk.Scrollbar(master=master, command=self.yview)
        sb.grid(column = x+1, row = y, sticky='nsew')

        #enable select_all
        self.bind("<Command-Key-a>", self.select_all)
        self.bind("<Command-Key-A>", self.select_all) # just in case caps lock is on

    #Get the value of the text
    def getVal(self):
        return self.get(1.0, tk.END) #1.0 first line, first character

    def select_all(self, event):
        #select all the text
        self.tag_add(tk.SEL, "1.0", tk.END) #tag SEL as the staring 1.0 and the END
        #move the crusor to the begining
        self.mark_set(tk.INSERT, tk.END)
        self.see(tk.INSERT)

if __name__ == '__main__':
    frame = tk.Tk()
    frame.grid()
    a = LabelWidget(frame, 0, 0, "test")
    a = EntryWidget(frame, 0, 1, "default value")

    text = TextWidget(frame, 1, 1, 10, 10, "testing")
    print text.getVal()

    def prt():
        print text.getVal()

    b = tk.Button(frame, text="print", command = prt)

    b.grid(column = 1, row=2)
    frame.mainloop()
