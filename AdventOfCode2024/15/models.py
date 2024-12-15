from enum import Enum


class ElementType(Enum):
    WALL = "#"
    ROBOT = "@"
    BOX = "O"
    EMPTY = "."


class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add_x(self, amount: int):
        return Position(x=self.x + amount, y=self.y)

    def add_y(self, amount: int):
        return Position(y=self.y + amount, x=self.x)

    def __eq__(self, value):
        if not isinstance(value, Position):
            return False

        return value.x == self.x and value.y == self.y

    def __str__(self):
        return f"Position(row:{self.x}, col:{self.y})"

    def __repr__(self):
        return str(self)


class Movement(str, Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"
