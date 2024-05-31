from src.models.order_item import OrderItem
from typing import List


class Order:
    def __init__(self, items: List[OrderItem] | None = None, payment_method: str = None, user_id: int = None):
        _items = items if items else list()
        self.items = _items
        self.payment_method = payment_method
        self.user_id = user_id

    def is_empty(self):
        return not self.items
