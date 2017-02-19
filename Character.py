from CharacterApp import CharacterApp
from Entity import Entity
from Classes import Levels

class Character(Entitiy):
    def __init__(self):
        Entity.__init__(self)

        self.health = None
        self.name = None
        self.race = None
        self.levels = Levels()

        self.app=CharacterApp(self)


    def startapp(self):
        self.app.start()
