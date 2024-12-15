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

    def __eq__(self, value):
        if not isinstance(value, Position):
            return False

        return value.x == self.x and value.y == self.y


class Movement(str, Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"
