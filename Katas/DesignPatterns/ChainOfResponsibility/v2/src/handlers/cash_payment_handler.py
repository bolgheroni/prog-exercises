from src.handlers.handler import Handler

class CashPaymentHandler(Handler):
    def handle(self, order):
        return self.next_handler.handle(order)

    def set_next(self, next_handler: Handler):
        self.next_handler = next_handler
        return self