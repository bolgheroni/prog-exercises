from src.handlers.base_handler import BaseHandler
from src.models.handle_result import HandleResult
from src.models.order import Order

class CashPaymentHandler(BaseHandler):
    def __init__(self, user_funds_service):
        super().__init__()
        self.user_funds_service = user_funds_service

    def _handle_specific(self, order):
        enough_cash_result = self._check_user_has_enough_cash(order.user_id, order)

        if enough_cash_result:
            return enough_cash_result

        return HandleResult(is_valid=True)

    def _check_user_has_enough_cash(self, user_id: str, order: Order) -> HandleResult | None:
        user_cash = self.user_funds_service.get_user_cash(user_id)
        order_total = order.get_total()

        if user_cash < order_total:
            return HandleResult(is_valid=False, cause="Funds aren't enough")

        return None

    def _can_handle(self, order):
        return order.payment_method == "cash"