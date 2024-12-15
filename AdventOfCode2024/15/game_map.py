from abc import ABC, abstractmethod
from models import Position, ElementType


class GameMap(ABC):
    @abstractmethod
    def check_position(self, position: Position) -> ElementType: ...

    @abstractmethod
    def set_element(self, position: Position, element: ElementType): ...


class EmptyGameMap(GameMap):
    def check_position(self, position):
        return ElementType.EMPTY

    def set_element(self, position, element):
        pass


class RowsGameMap(GameMap):
    def __init__(self, rows: list[list[ElementType]]):
        self._rows = rows

    def check_position(self, position: Position):
        return self._rows[position.x][position.y]

    def set_element(self, position: Position, element: ElementType):
        self._rows[position.x][position.y] = element

    def __str__(self):
        output = ""

        for row in self._rows:
            for element in row:
                output += element.value

            output += "\n"

        return output
