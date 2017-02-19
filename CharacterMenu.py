from Tkinter import *


class CharacterMenu:
    def __init__(self, master, character_list):
        self.character_list = character_list

        self.f_characters = Frame(master)
        self.f_characters.pack(fill=BOTH, expand=1, pady = 15, padx = 15)

        self.f_characters.columnconfigure(1, weight=2)
        self.f_characters.rowconfigure(1, weight=2)


        self.l_characters = Label(self.f_characters, text="Characters")
        self.l_characters.grid(row=0, column=0, columnspan=2)

        self.b_openall = Button(self.f_characters, text="Open All", command=self.openAll)
        self.b_openall.grid(row=1, column=0, sticky=N)

        self.ls_characters = Listbox(self.f_characters)
        self.ls_characters.grid(row=1, column=1, sticky=N+S+W+E)

        for character in self.character_list:
            self.ls_characters.insert(END, character.name)

        self.ls_characters.bind("<Double-Button-1>", self.openCharacter)

    def openCharacter(self, t):
        for character_index in self.ls_characters.curselection():
            self.character_list[character_index].startapp()


    def openAll(self):
        for character in self.character_list:
            character.startapp()
