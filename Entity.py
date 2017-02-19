from Attributes import Attributes
from Health import Health
from Transient import Transient

class Entity:
    def __init__(self):
        self.attr = Attributes()

        self.health = Health()
        self.transient = Transient()
