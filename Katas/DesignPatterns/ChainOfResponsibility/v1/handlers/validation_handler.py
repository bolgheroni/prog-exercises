from handlers.base_handler import BaseHandler
from models.order import Order
from models.handle_result import HandleResult

class ValidationHandler(BaseHandler):
    def handle(self, order: Order) -> HandleResult:
        result = self.validate_products_length(order)
        if result:
            return result

        result = self.validate_products_amount(order)
        if result:
            return result

        return super().handle(order)

    def validate_products_length(self, order: Order) -> HandleResult | None:
        if not order.products:
            return HandleResult(success=False, message="No products in order")
        return None

    def validate_products_amount(self, order: Order) -> HandleResult | None:
        for product in order.products:
            if product["amount"] <= 0:
                return HandleResult(success=False, message="Product amount is invalid")
        return None
