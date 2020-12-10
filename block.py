import random

TABLE = None

class Block:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.above = None
        self.below = TABLE
        self.color = self._get_rcolor()
        self.x = x
        self.y = y

    def _get_rcolor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    @property
    def on_table(self):
        return self.below == TABLE

    @property
    def clear(self):
        return self.above == None

    def __repr__(self):
        if self.on_table:
            return f'{self.name} is on table'
        else:
            return f'{self.name} is on blocks {self.below}'
