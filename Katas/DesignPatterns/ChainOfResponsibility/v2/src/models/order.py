from src.models.order_item import OrderItem
from typing import List


class Order:
    def __init__(self, items: List[OrderItem] | None = None):
        _items = items if items else list()
        self.items = _items

    def is_empty(self):
        return not self.items
