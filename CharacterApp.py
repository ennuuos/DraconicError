from Tkinter import *

class CharacterApp:
    def __init__(self, character):
        self.top = None
        self.character = character
    def start(self):
        if self.top is None:
            self.top = Toplevel()
            self.top.protocol('WM_DELETE_WINDOW', self.removewindow)


            self.l_name = Label(self.top, text="Name:")
            self.l_name.grid(row = 0, column = 0)

            self.l_name = Label(self.top, text=self.character.name)
            self.l_name.grid(row = 0, column = 1)

            self.l_name = Label(self.top, text="Player:")
            self.l_name.grid(row = 1, column = 0)

            self.l_name = Label(self.top, text=self.character.player)
            self.l_name.grid(row = 1, column = 1)

    def removewindow(self):
        self.top.destroy()
        self.top = None
