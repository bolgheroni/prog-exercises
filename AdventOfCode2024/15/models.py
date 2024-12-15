from enum import Enum


class ObjectType(Enum):
    WALL = "#"
    ROBOT = "@"
    BOX = "O"
    BOX_L = "["
    BOX_R = "]"
    EMPTY = "."


class Movement(str, Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


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

    def move(self, movement: Movement):
        match movement:
            case Movement.RIGHT:
                return self.add_y(1)
            case Movement.DOWN:
                return self.add_x(1)
            case Movement.LEFT:
                return self.add_y(-1)
            case Movement.UP:
                return self.add_x(-1)

    def __eq__(self, value):
        if not isinstance(value, Position):
            return False

        return value.x == self.x and value.y == self.y

    def __str__(self):
        return f"Position(row:{self.x}, col:{self.y})"

    def __repr__(self):
        return str(self)
