from CharacterApp import CharacterApp
from Entity import Entity

class Character(Entity):
    def __init__(self):
        Entity.__init__(self)

        self.health = None
        self.name = None
        self.race = None
        self.level = None

        self.app=CharacterApp(self)


    def startapp(self):
        self.app.start()
