import Tkinter as tk
from PIL import Image, ImageTk


class Window(tk.Frame):
    def __init__(self, parent, backgroundpic, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent    = parent
        self.width     = self.parent.winfo_screenwidth()
        self.height    = self.parent.winfo_screenheight() #returns current laptop/computer/anything screen resolution values
        self.parent.geometry ("%dx%d"%(self.width, self.height))
        self.bg = 'black'
        self.grid(column = 0, row = 0)
        #self.place (x = 0, y = 0, relwidth = 1, relheight = 1)
        self.defwidth  = 1366.0
        self.defheight = 768.0 #My laptop res. Will show why defined in the ASH ASV later
        self.backgroundpic = ImageTk.PhotoImage((Image.open(backgroundpic)).resize((self.width, self.height), Image.ANTIALIAS))
        self.bg_label = tk.Label(self, image = self.backgroundpic)
        #self.bg_label.place (x = 0, y = 0, relwidth = 1, relheight = 1)
        #self.bg_label.image = self.backgroundpic
        self.main = tk.Frame(self)
        self.main.grid(column = 0, row = 0, pady = (250, 0))
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        #self.bind("<Button-1>", self.callback)
        #self.main.bind("<Button-1>", self.callback)
        #self.parent.bind("<Button-1>", self.callback)

        #self.parent.columnconfigure(0, weight = 1)#; self.parent.rowconfigure(0, weight = 1)
        #self.parent.bind("<Button-1>", self.callback)

    @staticmethod
    def callback(event):
        print event.x, event.y

    def screensize(self):
        width = self.width
        height = self.height
        print width, height

#if __name__ == "__main__":
root = tk.Tk()
root.configure(background = 'black')
bgimage = "Quiz.jpg"
new = Window(root, bgimage)
new.configure(background = 'black')
new.main.configure(background = 'black')

#main.parent.geometry((main.width-500, main.height-500))
#main.parent.minsize(main.width-200, main.height-100)


'''class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = Statusbar(self, ...)
        self.toolbar = Toolbar(self, ...)
        self.navbar = Navbar(self, ...)
        self.main = Main(self, ...)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)'''

'''       self.parent = parent
        # <create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()'''
