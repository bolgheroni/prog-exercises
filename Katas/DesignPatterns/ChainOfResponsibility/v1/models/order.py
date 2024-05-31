
class Order():
    def __init__(self, products=None, buyer=None, delivery_address=None, payment_method=None, payment_details=None):
        self.products = products
        self.buyer = buyer
        self.delivery_address = delivery_address
        self.payment_method = payment_method
        self.payment_details = payment_details

    def total_price(self):
        return sum([product['price'] for product in self.products])