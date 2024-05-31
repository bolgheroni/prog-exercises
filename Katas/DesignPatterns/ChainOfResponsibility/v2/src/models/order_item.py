class OrderItem:
    def __init__(self, product: str, quantity: int, price: float | None = None):
        self.product = product
        self.quantity = quantity
        self.price = price