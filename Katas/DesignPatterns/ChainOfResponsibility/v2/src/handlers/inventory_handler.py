from src.models.handle_result import HandleResult
from src.models.order import Order
from src.handlers.base_handler import BaseHandler

class InventoryHandler(BaseHandler):
    def __init__(self, inventory):
        super().__init__()
        self.inventory = inventory

    def _handle_specific(self, order: Order) -> HandleResult:
        for item in order.items:
            if not self.inventory.is_available(item):
                return HandleResult(is_valid=False, cause=f"Unavailable quantity ({item.quantity}) product {item.product}")
        
        return HandleResult(is_valid=True)
    
    def _can_handle(self, order: Order) -> bool:
        return True