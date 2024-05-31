from src.models.handle_result import HandleResult
from src.handlers.handler import Handler
class FakeHandlersChain(Handler):
    def __init__(self):
        self.handle_calls = []
        self.handle_result = HandleResult(is_valid=False)
        super().__init__()

    def handle_called_with(self, order):
        return order in self.handle_calls

    def handle(self, order) -> HandleResult:
        self.handle_calls.append(order)
        return self.handle_result

    def with_valid_order(self):
        self.handle_result = HandleResult(is_valid=True)
        return self

    def with_invalid_order(self, cause):
        self.handle_result = HandleResult(is_valid=False, cause=cause)
        return self