from abc import ABC, abstractmethod
from src.models.handle_result import HandleResult
from src.models.order import Order
class Handler(ABC):
    @abstractmethod
    def handle(self, order: Order) -> HandleResult:
        pass