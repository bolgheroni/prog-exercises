from handlers.order_handler import OrderHandler
from models.order import Order
from models.handle_result import HandleResult

class BaseHandler(OrderHandler):
    def __init__(self):
        self.next = None

    def set_next(self, next_handler: OrderHandler) -> OrderHandler:
        self.next = next_handler
        return self

    def handle(self, order: Order) -> HandleResult:
        if self.next:
            return self.next.handle(order)
        else:
            return HandleResult(success=True)
