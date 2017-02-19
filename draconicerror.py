from Tkinter import *
from Character import *
from CharacterMenu import *

class App:
    def __init__(self, master):

        self.init_data()

        self.f_main = Frame(master)
        self.f_main.pack(fill=BOTH, expand=1)

        self.f_toolbar = Frame(self.f_main)
        self.f_toolbar.pack(side=TOP, fill=X)

        self.b_quit = Button(self.f_toolbar, text="Quit", command=self.f_main.quit)
        self.b_quit.pack(side=LEFT)

        CharacterMenu(self.f_main, self.characters)

    def init_data(self):
        self.characters = [
            Character(),
            Character(),
            Character()
        ]
        self.characters[0].name = "Kerry"
        self.characters[1].name = "Jonothan"
        self.characters[2].name = "Azaroth, Destroyer of Gods and Devourer of Worlds"

        self.characters[0].player = "Liam"
        self.characters[1].player = "Travis"
        self.characters[2].player = "Tom"


root = Tk()

app = App(root)

root.mainloop()
