class FakeHandlersChain:
    def __init__(self):
        self.handle_calls = []

    def handle_called_with(self, order):
        return order in self.handle_calls

    def handle(self, order):
        self.handle_calls.append(order)