from src.handlers.base_handler import BaseHandler
from src.models.handle_result import HandleResult
from src.models.order import Order


class ValidationHandler(BaseHandler):
    def _handle_specific(self, order: Order) -> HandleResult:
        empty_order_result = self._check_order_is_empty(order)
        if empty_order_result:
            return empty_order_result

        invalid_quantities_result = self._check_order_items_quantities(order)
        if invalid_quantities_result:
            return invalid_quantities_result

        invalid_prices_result = self._check_order_items_prices(order)
        if invalid_prices_result:
            return invalid_prices_result

        return HandleResult(is_valid=True)

    def _check_order_is_empty(self, order: Order) -> HandleResult | None:
        if order.is_empty():
            return HandleResult(is_valid=False, cause="Empty order")
        return None

    def _check_order_items_quantities(self, order: Order) -> HandleResult | None:
        for item in order.items:
            if item.quantity <= 0:
                return HandleResult(is_valid=False, cause=f"Invalid quantity ({item.quantity}) for {item.product}")
        return None

    def _check_order_items_prices(self, order: Order) -> HandleResult | None:
        for item in order.items:
            if item.price and item.price <= 0:
                return HandleResult(is_valid=False, cause=f"Invalid price ({item.price}) for {item.product}")
        return None
    
    def _can_handle(self, order: Order) -> bool:
        return True
