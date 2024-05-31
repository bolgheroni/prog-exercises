from src.models.order_item import OrderItem
class Inventory():
    def __init__(self, items):
        self.items = items

    def is_available(self, order_item: OrderItem):
        inventory_item = next((item for item in self.items if item["product"] == order_item.product), None)

        return inventory_item["quantity"] >= order_item.quantity