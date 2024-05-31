from handlers.base_handler import BaseHandler

class CashPaymentHandler(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self, order):
        if order.payment_method == "cash":
            cash_payment_details = order.payment_details
            result = self.check_available_cash(order, cash_payment_details)
            if result:
                return result
        return super().handle(order)
    
    def check_available_cash(self, order, cash_payment_details):
        if cash_payment_details['available_cash'] < order.total_price():
            return self.fail_response("Not enough cash")
        return None
            