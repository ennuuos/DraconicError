from Tkinter import *

from Attributes import Attributes

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

            self.l_player = Label(self.top, text="Player:")
            self.l_player.grid(row = 1, column = 0)

            self.l_player = Label(self.top, text=self.character.player)
            self.l_player.grid(row = 1, column = 1)

            self.placeAttributes()

    def placeAttributes(self):
        self.l_attr = Label(self.top, text="STR:")
        self.l_attr.grid(row = 2, column = 0)
        self.l_attrv = Label(self.top, text=self.attrformat(self.character.attr.str))
        self.l_attrv.grid(row = 2, column = 1)


        self.l_attr = Label(self.top, text="DEX:")
        self.l_attr.grid(row = 3, column = 0)
        self.l_attrv = Label(self.top, text=self.attrformat(self.character.attr.dex))
        self.l_attrv.grid(row = 3, column = 1)

        self.l_attr = Label(self.top, text="CON:")
        self.l_attr.grid(row = 4, column = 0)
        self.l_attrv = Label(self.top, text=self.attrformat(self.character.attr.con))
        self.l_attrv.grid(row = 4, column = 1)

        self.l_attr = Label(self.top, text="INT:")
        self.l_attr.grid(row = 5, column = 0)
        self.l_attrv = Label(self.top, text=self.attrformat(self.character.attr.int))
        self.l_attrv.grid(row = 5, column = 1)

        self.l_attr = Label(self.top, text="WIS:")
        self.l_attr.grid(row = 6, column = 0)
        self.l_attrv = Label(self.top, text=self.attrformat(self.character.attr.wis))
        self.l_attrv.grid(row = 6, column = 1)

        self.l_attr = Label(self.top, text="CHA:")
        self.l_attr.grid(row = 7, column = 0)
        self.l_attrv = Label(self.top, text=self.attrformat(self.character.attr.cha))
        self.l_attrv.grid(row = 7, column = 1)

    def attrformat(self, ability):
        return str(ability) + " (" + str(Attributes.modifier(ability)) + ')'

    def removewindow(self):
        self.top.destroy()
        self.top = None
