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
        return int(value / 2 - 5)

    @staticmethod
    def proficiency(level):
        return int((level-1)/4+2)
