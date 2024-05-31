from abc import ABC, abstractmethod
from src.models.handle_result import HandleResult

class Handler(ABC):
    @abstractmethod
    def handle(self, order) -> HandleResult:
        pass