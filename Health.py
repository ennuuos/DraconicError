class Health:
    def __init__(self):

        self.max = None
        self.current = None
        self.temp = None

    def clamp(self):
        self.current = min(self.max, self.current)

    def heal(self, amount):
        self.current += amount
        self.clamp()

    def damage(self, amount):
        self.temp = max(0, temp-amount)
        self.current += min(0, temp-amount)
        self.clamp()

    def increase(self, amount):
        self.max += amount
