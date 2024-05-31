from src.models.handle_result import HandleResult
from src.models.order import Order

class InventoryHandler():
    def __init__(self, inventory):
        self.inventory = inventory

    def handle(self, order: Order) -> HandleResult:
        for item in order.items:
            if not self.inventory.is_available(item):
                return HandleResult(is_valid=False, cause=f"Unavailable quantity ({item.quantity}) product {item.product}")
        
        return HandleResult(is_valid=True)