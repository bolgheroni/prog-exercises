from src.handlers.handler import Handler
from src.models.handle_result import HandleResult


class CashPaymentHandler(Handler):
    def __init__(self, user_funds_service):
        super().__init__()
        self.user_funds_service = user_funds_service
        self.next_handler = None

    def handle(self, order):
        if self.next_handler:
            return self.next_handler.handle(order)
        return HandleResult(is_valid=False, cause="Funds aren't enough")

    def set_next(self, next_handler: Handler):
        self.next_handler = next_handler
