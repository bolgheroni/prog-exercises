from src.models.handle_result import HandleResult
from src.handlers.base_handler import BaseHandler
class FakeHandler(BaseHandler):
    def __init__(self):
        self.handle_calls = []
        self.handle_result = HandleResult(is_valid=False)
        self.can_handle_result = True
        super().__init__()

    def handle_called_with(self, order):
        return order in self.handle_calls

    def _handle_specific(self, order) -> HandleResult:
        self.handle_calls.append(order)
        return self.handle_result

    def with_valid_order(self):
        self.handle_result = HandleResult(is_valid=True)
        return self

    def with_invalid_order(self, cause):
        self.handle_result = HandleResult(is_valid=False, cause=cause)
        return self
    
    def with_None_result(self):
        self.handle_result = None
        self.can_handle_result = False
        return self
    
    def _can_handle(self, order) -> bool:
        return self.can_handle_result
        