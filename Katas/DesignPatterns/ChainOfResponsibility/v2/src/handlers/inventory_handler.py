from src.models.handle_result import HandleResult
from src.models.order import Order

class InventoryHandler():
    def __init__(self, inventory):
        self.inventory = inventory

    def handle(self, order: Order) -> HandleResult:

        return HandleResult(is_valid=False, cause=f"Unavailable quantity ({order.items[0].quantity}) product {order.items[0].product}")