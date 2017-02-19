from math import *

class Attributes:
    def __init__(self):
        self.str = 10
        self.dex = 10
        self.con = 10
        self.int = 10
        self.wis = 10
        self.cha = 10
    @staticmethod
    def modifier(value):
        return int(floor(value / 2 - 5))
