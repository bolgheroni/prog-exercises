from src.handlers.handler import Handler
from src.models.handle_result import HandleResult
from src.models.order import Order
class ValidationHandler(Handler):
    def handle(self, order: Order) -> HandleResult:
        if order.is_empty():
            return HandleResult(is_valid=False, cause="Empty order")
        
        return HandleResult(is_valid=True)