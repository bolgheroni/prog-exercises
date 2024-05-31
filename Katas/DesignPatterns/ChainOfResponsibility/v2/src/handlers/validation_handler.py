from src.handlers.handler import Handler
from src.models.handle_result import HandleResult

class ValidationHandler(Handler):
    def handle(self, order) -> HandleResult:
        return HandleResult(False, "Empty order")