from abc import ABC, abstractmethod
from models.order import Order
from models.handle_result import HandleResult

class OrderHandler(ABC):
    @abstractmethod
    def handle(self, order: Order) -> HandleResult:
        pass
