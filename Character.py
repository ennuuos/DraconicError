from CharacterApp import CharacterApp
class Character:
    def __init__(self):

        self.health = None
        self.name = None
        self.race = None
        self.app=CharacterApp(self)

    def startapp(self):
        self.app.start()
