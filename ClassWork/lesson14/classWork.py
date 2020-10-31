class Chessman:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def __repr__(self):
        return f"I am {self.color} on {self.position}"


class Pawn(Chessman):
    def __init__(self, position, color):
        super().__init__(position, color)
        self.is_Queen = False

    def __repr__(self):
        return f"I am {self.color} Pawn on {self.position}"


piece = Chessman('A2', 'White')
pawn = Pawn('G2', 'Black')

print(piece)
print(pawn)
