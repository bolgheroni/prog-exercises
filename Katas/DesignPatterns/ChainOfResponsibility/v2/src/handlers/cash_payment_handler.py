from src.handlers.handler import Handler
from src.models.handle_result import HandleResult
from src.models.order import Order


class CashPaymentHandler(Handler):
    def __init__(self, user_funds_service):
        super().__init__()
        self.user_funds_service = user_funds_service
        self.next_handler = None

    def handle(self, order):
        if order.payment_method != "cash":
            return self._next_handler_result(order)
            
        enough_cash_result = self._check_user_has_enough_cash(order.user_id, order)

        if enough_cash_result:
            return enough_cash_result

        next_handler_result = self._next_handler_result(order)

        if next_handler_result:
            return next_handler_result

        return HandleResult(is_valid=True)

    def set_next(self, next_handler: Handler):
        self.next_handler = next_handler

    def _check_user_has_enough_cash(self, user_id: str, order: Order) -> HandleResult | None:
        user_cash = self.user_funds_service.get_user_cash(user_id)
        order_total = order.get_total()

        if user_cash < order_total:
            return HandleResult(is_valid=False, cause="Funds aren't enough")

        return None

    def _next_handler_result(self, order):
        if self.next_handler:
            return self.next_handler.handle(order)
        return None