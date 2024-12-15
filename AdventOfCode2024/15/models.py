from enum import Enum


class ElementType(Enum):
    WALL = 0
    ROBOT = 1
    BOX = 2
    EMPTY = 3


class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Movement(str, Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"
