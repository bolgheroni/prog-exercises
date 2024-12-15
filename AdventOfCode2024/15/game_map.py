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
