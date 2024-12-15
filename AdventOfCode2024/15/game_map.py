from abc import ABC, abstractmethod
from models import Position, ObjectType


class GameMap(ABC):
    @abstractmethod
    def check_position(self, position: Position) -> ObjectType: ...

    @abstractmethod
    def set_object(self, position: Position, object: ObjectType): ...

    @abstractmethod
    def get_robot_position(self) -> Position: ...

    @abstractmethod
    def calculate_score(self) -> int: ...


class EmptyGameMap(GameMap):
    def check_position(self, position):
        return ObjectType.EMPTY

    def set_object(self, position, object):
        pass

    def get_robot_position(self):
        return Position(0, 0)

    def calculate_score(self):
        return 0


class RowsGameMap(GameMap):
    def __init__(self, rows: list[list[ObjectType]]):
        self._rows = rows

    def check_position(self, position: Position):
        return self._rows[position.x][position.y]

    def set_object(self, position: Position, object: ObjectType):
        self._rows[position.x][position.y] = object

    def get_robot_position(self):
        i = 0
        for i in range(0, len(self._rows)):
            for j in range(0, len(self._rows[0])):
                pos = Position(i, j)
                if self.check_position(pos) == ObjectType.ROBOT:
                    return pos

        raise Exception("Robot not found")

    def __str__(self):
        output = ""

        for row in self._rows:
            for object in row:
                output += object.value

            output += "\n"

        return output

    def calculate_score(self):
        score = 0
        i = 0
        for i in range(0, len(self._rows)):
            for j in range(0, len(self._rows[0])):
                pos = Position(i, j)
                if self.check_position(pos) == ObjectType.BOX:
                    score += i * 100 + j

        return score
