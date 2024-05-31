from src.handlers.handler import Handler
from src.models.handle_result import HandleResult


class CashPaymentHandler(Handler):
    def __init__(self, user_funds_service):
        super().__init__()
        self.user_funds_service = user_funds_service
        self.next_handler = None

    def handle(self, order):
        order_total = order.get_total()
        user_cash = self.user_funds_service.get_user_cash(order.user_id)

        if user_cash < order_total:
            return HandleResult(is_valid=False, cause="Funds aren't enough")
        
        if self.next_handler:
            return self.next_handler.handle(order)
        
        return HandleResult(is_valid=True)

    def set_next(self, next_handler: Handler):
        self.next_handler = next_handler
