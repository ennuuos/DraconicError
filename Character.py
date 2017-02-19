from CharacterApp import CharacterApp

class Entity:
    def __init__(self):

        self.str = 10
        self.dex = 10
        self.con = 10
        self.int = 10
        self.wis = 10
        self.cha = 10


class Character(Entity):
    def __init__(self):

        self.health = None
        self.name = None
        self.race = None
        self.app=CharacterApp(self)

    def startapp(self):
        self.app.start()
