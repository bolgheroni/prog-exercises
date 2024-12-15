from abc import ABC, abstractmethod
from models import Position, ElementType


class GameMap(ABC):
    @abstractmethod
    def check_position(self, position: Position) -> ElementType: ...

    @abstractmethod
    def set_element(self, position: Position, element: ElementType): ...

    @abstractmethod
    def get_robot_position(self) -> Position: ...


class EmptyGameMap(GameMap):
    def check_position(self, position):
        return ElementType.EMPTY

    def set_element(self, position, element):
        pass

    def get_robot_position(self):
        return Position(0, 0)


class RowsGameMap(GameMap):
    def __init__(self, rows: list[list[ElementType]]):
        self._rows = rows

    def check_position(self, position: Position):
        return self._rows[position.x][position.y]

    def set_element(self, position: Position, element: ElementType):
        self._rows[position.x][position.y] = element

    def get_robot_position(self):
        i = 0
        for i in range(0, len(self._rows)):
            for j in range(0, len(self._rows[0])):
                pos = Position(i, j)
                if self.check_position(pos) == ElementType.ROBOT:
                    return pos

        raise Exception("Robot not found")

    def __str__(self):
        output = ""

        for row in self._rows:
            for element in row:
                output += element.value

            output += "\n"

        return output
