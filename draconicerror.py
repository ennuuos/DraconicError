from Tkinter import *
from Character import *
from CharacterMenu import *

class App:
    def __init__(self, master):

        self.init_data()

        self.f_main = Frame(master)
        self.f_main.pack()

        self.f_toolbar = Frame(self.f_main)
        self.f_toolbar.pack(side=TOP, fill=X)

        self.b_quit = Button(self.f_toolbar, text="Quit", command=self.f_main.quit)
        self.b_quit.pack(side=LEFT)

        CharacterMenu(self.f_main, self.characters)

    def init_data(self):
        self.characters = []


root = Tk()

app = App(root)

root.mainloop()
