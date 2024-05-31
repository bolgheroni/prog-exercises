from src.handlers.handler import Handler
from src.models.handle_result import HandleResult
from src.models.order import Order
class ValidationHandler(Handler):
    def handle(self, order: Order) -> HandleResult:
        if order.is_empty():
            return HandleResult(is_valid=False, cause="Empty order")
        for item in order.items:
            if item.quantity <= 0:
                return HandleResult(is_valid=False, cause=f"Invalid quantity ({item.quantity}) for {item.product}")
        return HandleResult(is_valid=True)