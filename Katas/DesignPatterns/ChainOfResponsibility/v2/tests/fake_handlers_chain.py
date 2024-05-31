from src.models.handle_result import HandleResult

class FakeHandlersChain:
    def __init__(self):
        self.handle_calls = []

    def handle_called_with(self, order):
        return order in self.handle_calls

    def handle(self, order) -> HandleResult:
        self.handle_calls.append(order)
        return HandleResult(is_valid=True)

    def with_valid_order(self):
        return self