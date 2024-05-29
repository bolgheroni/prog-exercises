from .base_handler import BaseHandler
from models.order import Order
from models.handle_result import HandleResult

class InventoryHandler(BaseHandler):
    def __init__(self, inventory):
        super().__init__()
        self.inventory = inventory

    def handle(self, order: Order) -> HandleResult:
        result = self.check_inventory(order)
        if result:
            return result

        return super().handle(order)

    def check_inventory(self, order: Order) -> HandleResult | None:
        for product in order.products:
            if product["name"] not in [item["name"] for item in self.inventory]:
                return HandleResult(success=False, message=f"Product {product['name']} is not in inventory")
            
            inventory_product = next(item for item in self.inventory if item["name"] == product["name"])
            
            if inventory_product["amount"] <= 0:
                return HandleResult(success=False, message=f"Product {product['name']} is out of stock")
            
            if product["amount"] > inventory_product["amount"]:
                return HandleResult(success=False, message=f"Product {product['name']} stock amount is not sufficient")
            
        return None

