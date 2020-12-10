class STATES:

    def __init__(self):
        self.name = self.__class__.__name__
        if self.name == 'ON_TABLE':
            self.priority = 0
        elif self.name == 'ON':
            self.priority = 1
        elif self.name == 'CLEAR':
            self.priority = 2

    @property
    def is_satisfied(self):
        blocks = self.blocks
        if self.name == 'CLEAR':
            return blocks[self.what].clear
        elif self.name == 'ON_TABLE':
            return blocks[self.what].on_table
        elif self.name == 'ON':
            return blocks[self.top].below == self.bottom

    def construct(self):
        blocks = self.blocks
        name = self.__class__.__name__
        if self.name == 'ON':
            blocks[self.top].below = self.bottom
            blocks[self.bottom].above = self.top

    def work(self):
        blocks = self.blocks
        if self.name == 'ON_TABLE':
            self.unstack(self.what)
        elif self.name == 'ON':
            self.stack(self.top, self.bottom)


    def unstack(self, what):
        blocks = self.blocks
        # condition of on_table is clear and armempty
        while not blocks[what].clear:
            self.unstack(blocks[what].above)
        print(f'UNSTACK({what})')
        below = blocks[what].below
        blocks[what].below = None
        blocks[below].above = None

    def stack(self, top, bottom):
        blocks = self.blocks
        # condition of on is the top and bottom both are clear
        if not blocks[top].clear:
            self.unstack(blocks[top].above)
        if not blocks[bottom].clear:
            self.unstack(blocks[bottom].above)
        print(f'STACK({top}, {bottom})')
        below = blocks[top].below
        blocks[bottom].above = top
        blocks[top].below = bottom
        if below:
            blocks[below].above = None


class CLEAR(STATES):

    def __init__(self, what):
        self.what = what
        super().__init__()

    def __repr__(self):
        return f'CLEAR({self.what})'


class ON_TABLE(STATES):

    def __init__(self, what):
        self.what = what
        super().__init__()

    def __repr__(self):
        return f'ONTABLE({self.what})'


class ON(STATES):

    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
        super().__init__()

    def __repr__(self):
        return f'ON({self.top}, {self.bottom})'

