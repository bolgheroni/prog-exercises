
class Order():
    def __init__(self, products=None, buyer=None, delivery_address=None, payment_method=None, order_details=None):
        self.products = products
        self.buyer = buyer
        self.delivery_address = delivery_address
        self.payment_method = payment_method
        self.order_details = order_details
